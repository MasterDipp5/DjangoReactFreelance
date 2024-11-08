from django.urls import path
from . import views
from .views import UserProfileView, RegisterView

urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('register/', RegisterView.as_view(), name='register'),
]
