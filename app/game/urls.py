from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'game'

urlpatterns = [
    # Concept
    path('concepts/', views.ConceptsView.as_view(), name='concept-list'),
    path('concept/new', views.ConceptCreateView.as_view(), name='concept-register'),
    path('concept/<uuid:pk>/edit', views.ConceptEditView.as_view(), name='concept-edit'),
    path('concept/<uuid:pk>/delete', views.concept_delete_view, name='concept-delete'),
]
