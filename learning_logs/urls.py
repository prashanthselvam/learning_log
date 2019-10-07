"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

urlpatterns = [
  # Home Page
  path('', views.index, name = 'index'),

  # Topics Page
  path('topics/', views.topics, name = 'topics'),

  # Detail Page for a single topic
  path('topics/<topic_id>/', views.topic_detail, name = 'topic_detail'),

  # Add new topic page
  path('new_topic/', views.new_topic, name = 'new_topic'),

  # Add new entry
  path('new_entry/<topic_id>', views.new_entry, name = 'new_entry'),

  # Edit an entry
  path('edit_entry/<entry_id>', views.edit_entry, name = 'edit_entry')

]