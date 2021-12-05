from rest_framework import serializers
from .models import Subject, Quiz, Question, Choice

# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = ['pk', 'subject']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'id',
            'text',
            'is_correct'
        ]


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()

    def get_choices(self, obj):
        ordered_queryset = Choice.objects.filter(question__id=obj.id).order_by('?')
        return ChoiceSerializer(ordered_queryset, many=True).data

    class Meta:
        model = Question
        fields = ['text', 'choices']


class QuizSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    def get_questions(self, args):
        print(self.instance.is_draft)
        questions_list = Question.objects.all().order_by('?')[:self.context['num']]
        return QuestionSerializer(questions_list, many=True).data

    class Meta:
        model = Quiz
        fields = ['title', 'subject', 'is_draft', 'questions']

# class QuestionSerializer(serializers.ModelSerializer):
#     subject = SubjectSerializer()
#     choices = ChoiceSerializer(many=True)
#     class Meta:
#         model = Question
#         fields = ['pk', 'subject', 'text', 'instruction', 'choices']


# class QuizSerializer(serializers.ModelSerializer):

#     questions = QuestionSerializer(many=True)
#     class Meta:
#         model = Quiz
#         fields = [
#             'title',
#             'subject',
#             'is_draft',
#             'questions'
#         ]
