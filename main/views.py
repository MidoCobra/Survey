from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Survey_Model, Question, Answer, Participant
from .forms import AnswerForm

@login_required
def SurveysView(request):
    user = request.user
    surveys = Survey_Model.objects.all().exclude(survey_participant__participant=user, survey_participant__submitted=True)
    context = {
        'surveys' : surveys
    }
    return render(request, 'surveys.html', context)

@login_required
def StartSurvey(request, survey_id):
    user = request.user
    survey = get_object_or_404(Survey_Model, id=survey_id)
    question = Question.objects.filter(survey = survey).exclude(question_answer__participant=user).first()
    context = {
        'question': question,
        'survey': survey,
    }
    

    return render(request, 'startSurvey.html', context)


@login_required
def AnswerView(request):
    user = request.user
    getQuestionId = request.GET.get('questionId')
    getQuestion = get_object_or_404(Question, id=getQuestionId)
    survey = get_object_or_404(Survey_Model, id=getQuestion.survey.id)

    if request.method == "GET":
        getAnswer = request.GET.get('answer')
        checkRepeatedAnswer = Answer.objects.filter(question=getQuestion, participant=user, answer__isnull=False)
        if checkRepeatedAnswer.exists(): 
            checkRemainingQuestions = Question.objects.filter(survey=survey).exclude(question_answer__participant=user)
            if checkRemainingQuestions.exists():
                nextQuestion = Question.objects.filter(survey=survey).exclude(question_answer__participant=user).first()
                context = {
                    'survey': survey,
                    'question': nextQuestion,
                }
                return render(request, 'answer.html', context)
            else:
                Participant.objects.update_or_create(participant=user, survey=survey, submitted=True)
                return render(request, 'thanks.html')
        else:
            Answer.objects.update_or_create(question=getQuestion, participant=user,answer=getAnswer)
            checkRemainingQuestions = Question.objects.filter(survey=survey).exclude(question_answer__participant=user)
            if checkRemainingQuestions.exists():
                nextQuestion = Question.objects.filter(survey=survey).exclude(question_answer__participant=user).first()
                context = {
                    'survey': survey,
                    'question': nextQuestion,
                }
                return render(request, 'answer.html', context)
            else:
                Participant.objects.update_or_create(participant=user, survey=survey, submitted=True)
                return render(request, 'thanks.html')

    return render(request, 'thanks.html')
