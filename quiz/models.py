from django.db import models


class Subject(models.Model):
    subject = models.CharField(
        max_length=400, blank=False, null=False
    )

    def __str__(self):
        return self.subject


class Quiz(models.Model):
    title = models.CharField(
        max_length=150, blank=False, null=False
    )
    subject = models.ForeignKey(
        'Subject', null=True, on_delete=models.SET_NULL
    )
    is_draft = models.BooleanField(
        blank=True, default=False
    )

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'
        ordering = ['pk']

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField(
        blank=False, null=False
    )
    instruction = models.TextField(
        blank=False, null=False
    )
    subject = models.ForeignKey(
        'Subject', blank=False, null=True, on_delete=models.SET_NULL
    )
    quiz = models.ManyToManyField(
        'Quiz', blank=False, related_name='questions'
    )

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['pk']

    def __str__(self):
        return self.text

class Choice(models.Model):
    text = models.TextField(
        blank=False, null=False
    )
    is_correct = models.BooleanField(
        blank=False, null=False
    )
    question = models.ForeignKey(
        'Question', 
        related_name='choices', 
        null=False, 
        blank=False, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text