# Overview

As a software developer, I am learning to build dynamic web applications with a server-side framework. For this module I built the Pupil Practice Portal with Python and Django. It is a practice quiz site for Primary 3 pupils.

A pupil enters their name, picks a subject (Maths or English) and a difficulty (Easy or Hard), and takes a short multiple-choice quiz. The server grades the answers, saves each attempt to a SQLite database through Django's ORM, and shows the score. A "Past Results" page lists every saved attempt, so a teacher can see how pupils are doing.

My purpose in writing this software was to learn how Django separates models, views, URLs and templates, and how a web app stores and retrieves data.

[Software Demo Video] ( https://youtu.be/2m6hnmMEp0E )

# Development Environment

- Python 3.14
- Django 6.1
- SQLite (Django's default database)
- Visual Studio Code
- Git and GitHub
- HTML and CSS (Django templates)

# Useful Websites

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial: Writing your first app](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [W3Schools Django Tutorial](https://www.w3schools.com/django/)
- [MDN Django Web Framework](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)

# How to Run

1. Install Django: `py -m pip install django`
2. In the project folder, run `py manage.py migrate`
3. Run `py manage.py runserver`
4. Open http://127.0.0.1:8000/ in a browser

# Future Work

- Add teacher login so only teachers can view past results
- Add more subjects (Science, OWOP, RME) and a bigger question bank
- Let teachers add questions through the Django admin
- Add charts showing each pupil's progress over time
