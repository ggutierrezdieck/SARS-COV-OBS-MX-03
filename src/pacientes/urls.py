from django.urls import path
from .views import index_view, questionnaire_view

urlpatterns = [
    path('', index_view, name='home'),
    path('q', questionnaire_view, name='questionario'),
]
