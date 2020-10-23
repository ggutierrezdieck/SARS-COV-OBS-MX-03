from django.urls import path
from .views import registerUser


urlpatterns = [
path('', registerUser, name='session'),
]
