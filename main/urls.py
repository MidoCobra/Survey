from django.urls import path  
from .views import SurveysView, StartSurvey, AnswerView
urlpatterns = [  
    path('', SurveysView, name='surveys'),
    path('survey/<int:survey_id>', StartSurvey, name='survey'),
    path('answer', AnswerView, name='answer'),
]  