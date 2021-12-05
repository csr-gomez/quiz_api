from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import Subject, Quiz, Question
from .serializers import QuestionSerializer, QuizSerializer
from rest_framework.response import Response


class StartQuiz(APIView):

    def get(self, request, **kwargs):
        quiz = Quiz.objects.get(subject__id=kwargs['category_id'])
        serializer = QuizSerializer(quiz, context=kwargs)
        return Response(serializer.data)

    # def get(self, request, **kwargs):
    #     quiz = Quiz.objects.get(subject__id=kwargs['category_id'])
    #     questions = quiz.questions.all().order_by('?')[:1]
    #     amount = 5
    #     context = {'category_id': kwargs['category_id'],
    #                 'amount': kwargs['num']
    #     }
    #     serializer = QuestionSerializer(
    #         questions, many=True, context=context
    #     )
    #     return Response(serializer.data)

# class SubjectListView(generics.ListAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer


# class QuizView(generics.RetrieveAPIView):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer


# class ListQuestionsView(APIView):

#     def get(self, request, format=None, **kwargs):
#         questions = Question.objects.filter(
#             subject__pk=kwargs['pk']
#         ).order_by('?')[:kwargs['num']]
#         serializer = QuestionSerializer(questions, many=True)
#         return Response(serializer.data)
