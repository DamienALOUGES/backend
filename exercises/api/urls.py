from django.urls import path

from .views import ExerciseListView, ExerciseDetailView

urlpatterns = [
    path('', ExerciseListView.as_view()),
    path('/<pk>', ExerciseDetailView.as_view())
]
