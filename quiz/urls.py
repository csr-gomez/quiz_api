from django.urls import path
from .views import StartQuiz

urlpatterns = [
    path('category=<int:category_id>&num=<int:num>/', StartQuiz.as_view()),
    # path(
    #     'subject=<str:pk>&num=<int:num>/', ListQuestionsView.as_view()
    # ),
    # path('subjects/', SubjectListView.as_view()),
    # path('quizzes/<int:pk>/', QuizView.as_view()),
    
]
