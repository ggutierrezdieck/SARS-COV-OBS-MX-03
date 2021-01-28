from django.urls import path
from .views import index_view,nuevo_view, questionnaire_view

urlpatterns = [
    path('', index_view, name='home'),
    path('n', nuevo_view, name='nuevo'),
    path('q/<int:id>', questionnaire_view, name='questionario'),
]
