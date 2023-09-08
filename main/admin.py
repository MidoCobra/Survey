from django.contrib import admin
from .models import Survey_Model, Question, Participant, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'question', 'type')
    list_filter = ('survey', 'type')
    search_fields = ('survey', 'question')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'participant']
    # list_filter = ('question__survey__title',)
    # search_fields = ('question__survey__title', 'participant')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['participant', 'survey']
    list_filter = ('survey',)
    
admin.site.register(Survey_Model)

