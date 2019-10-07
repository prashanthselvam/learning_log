"""Defines URL patterns for learning_logs."""

from django.urls import path, include

from . import views

urlpatterns = [
  # Sign Up Page
  path('signup/', views.signup, name = 'signup'),

  # Log In Page
  path('login/', include(('django.contrib.auth.urls','login'), namespace = 'login'))

]