# ============================================================
# views.py
# View functions for the Pupil Practice Portal.
# Handles the home form, the generated quiz page, grading the
# submitted answers, and showing past results from the database.
# ============================================================

from django.shortcuts import render, redirect
from .questions import get_questions
from .models import Attempt


def home(request):
    """
    Displays the home page with a form where a pupil enters their
    name and picks a subject and difficulty. This is a static page
    with no user input processing yet.
    """
    return render(request, "practice_portal/home.html")


def quiz(request):
    """
    Handles the submitted home page form (POST), looks up a matching
    set of practice questions, and renders them as a new quiz page.
    The pupil's name, subject, and difficulty are carried forward as
    hidden fields so they are available again when the quiz is graded.
    """
    if request.method != "POST":
        # If someone visits this URL directly without submitting the
        # form, send them back to the home page instead of erroring.
        return redirect("home")

    pupil_name = request.POST.get("pupil_name", "").strip()
    subject = request.POST.get("subject")
    difficulty = request.POST.get("difficulty")

    questions = get_questions(subject, difficulty)

    context = {
        "pupil_name": pupil_name,
        "subject": subject,
        "difficulty": difficulty,
        "questions": questions,
    }
    return render(request, "practice_portal/quiz.html", context)


def results(request):
    """
    Grades the submitted quiz answers against the question bank,
    saves the attempt to the database, and renders the results page
    showing the pupil's score. This is the module's interactive,
    database-backed core.
    """
    if request.method != "POST":
        return redirect("home")

    pupil_name = request.POST.get("pupil_name", "Pupil").strip() or "Pupil"
    subject = request.POST.get("subject")
    difficulty = request.POST.get("difficulty")

    questions = get_questions(subject, difficulty)
    score = _grade_answers(request.POST, questions)

    # Save this attempt so it shows up on the history page later.
    attempt = Attempt.objects.create(
        pupil_name=pupil_name,
        subject=subject,
        difficulty=difficulty,
        score=score,
        total_questions=len(questions),
    )

    context = {"attempt": attempt}
    return render(request, "practice_portal/results.html", context)


def _grade_answers(post_data, questions):
    """
    Compares each question's submitted answer (named q0, q1, q2, ...
    in the quiz form) against its correct answer and returns the
    total number of correct responses.
    """
    correct_count = 0
    for index, question in enumerate(questions):
        submitted = post_data.get(f"q{index}")
        if submitted == question["answer"]:
            correct_count += 1
    return correct_count


def history(request):
    """
    Queries the database for every past attempt, most recent first,
    and renders them on the "Past Results" page. This is the third
    dynamically generated page required by the module.
    """
    attempts = Attempt.objects.all().order_by("-completed_at")
    context = {"attempts": attempts}
    return render(request, "practice_portal/history.html", context)
