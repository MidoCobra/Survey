from django.db import models
from django.urls import reverse
from Survey import settings

class Survey_Model(models.Model):
    title = models.CharField(max_length=140, unique=True)
    description = models.TextField(max_length=400)
    start_at = models.DateField()
    end_at = models.DateField()

    def get_absolute_url(self):
        return reverse("survey", args=[str(self.id)])

    def __str__(self):
        return self.title


class Question(models.Model):
    TYPE_CHOICES =(
    ("1", "Radio"),
    ("2", "Select"),
    ("3", "Text")
    )

    helpTextChoice = "The Choice Field is only used if the question type is 'Radio' or 'select', YOU MUST PROVIDE A COMMA-SEPARTED LIST OF OPTIONS FOR THIS QUESTION"
    
    survey = models.ForeignKey(Survey_Model, on_delete=models.CASCADE, related_name="survey_question")
    question = models.CharField(max_length=3000, unique=True, blank=False)
    type = models.CharField(max_length=12, choices=TYPE_CHOICES, blank=False)
    choices = models.TextField(max_length=2000, blank=True, help_text= helpTextChoice)

    def get_absolute_url(self):
        return reverse("question", args=[str(self.id)])

    def __str__(self):
        return self.question


class Participant(models.Model):
    participant = models.ForeignKey(
        settings.AUTH_USER_MODEL, max_length=200, on_delete=models.CASCADE, related_name="user_answer", null=True, blank=True)
    survey = models.ForeignKey(Survey_Model, on_delete=models.CASCADE, related_name="survey_participant")
    submitted = models.BooleanField(default=False)

    def __str__(self):
        return self.participant.email



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_answer")
    # participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="participant_answer")
    participant = models.ForeignKey(
        settings.AUTH_USER_MODEL, max_length=200, on_delete=models.CASCADE, related_name="participant_answer", null=True, blank=True)
    answer = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.participant.email