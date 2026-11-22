# ============================================================
# models.py
# Database model for the Pupil Practice Portal.
# Each row records one pupil's completed quiz attempt.
# ============================================================

from django.db import models


class Attempt(models.Model):
    """
    Represents a single pupil's completed practice attempt:
    who took it, which subject/difficulty, and their score.
    """
    pupil_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=20)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a human-readable label used in Django admin and shell."""
        return f"{self.pupil_name} - {self.subject}/{self.difficulty}: {self.score}/{self.total_questions}"

    def percentage(self):
        """Returns the score as a rounded percentage for display in templates."""
        if self.total_questions == 0:
            return 0
        return round((self.score / self.total_questions) * 100)
