# ============================================================
# urls.py (app-level)
# Maps URL paths to their corresponding view functions for the
# Pupil Practice Portal app.
# ============================================================

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("quiz/", views.quiz, name="quiz"),
    path("results/", views.results, name="results"),
    path("history/", views.history, name="history"),
]
