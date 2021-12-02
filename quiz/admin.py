from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Quiz, Subject, Choice, Question


class ChoiceInine(admin.TabularInline):
    model = Choice


class QuizAdminForm(forms.ModelForm):

    class Meta:
        model = Quiz
        exclude = []
    
    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all(),
        required=True,
        label='Questions',
        widget=FilteredSelectMultiple(
            verbose_name='questions',
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(QuizAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = (
                self.instance.question_set.all()
            )

    def save(self, commit=True):
        quiz = super(QuizAdminForm, self).save(commit=False)
        quiz.save()
        quiz.question_set.set(self.cleaned_data['questions'])
        self.save_m2m()
        return quiz


class QuizAdmin(admin.ModelAdmin):
    form = QuizAdminForm

    list_display = ['title', 'subject']
    list_filter = ['subject']
    search_fields = ['subject']


class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['subject']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'subject']
    list_finter = ['subject']
    fields = ['text', 'instruction', 'subject', 'quiz']

    search_fields = ['content']
    filter_horizontal = ['quiz']

    inlines = [ChoiceInine]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Question, QuestionAdmin)