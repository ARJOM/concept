from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'game'

urlpatterns = [
    # Concept
    path('concepts/', views.ConceptsView.as_view(), name='concept-list'),
    path('concepts/deleted', views.ConceptsDeletedView.as_view(), name='concept-deleted'),
    path('concept/new', views.ConceptCreateView.as_view(), name='concept-register'),
    path('concept/<uuid:pk>/edit', views.ConceptEditView.as_view(), name='concept-edit'),
    path('concept/<uuid:pk>/delete', views.concept_delete_view, name='concept-delete'),
    path('concept/<uuid:pk>/activate', views.concept_activate_view, name='concept-activate'),

    # Item
    path('items/', views.ItemsView.as_view(), name='item-list'),
    path('items/deleted', views.ItemsDeletedView.as_view(), name='item-deleted'),
    path('item/new', views.ItemCreateView.as_view(), name='item-register'),
    path('item/<uuid:pk>/edit', views.ItemEditView.as_view(), name='item-edit'),
    path('item/<uuid:pk>/delete', views.item_delete_view, name='item-delete'),
    path('item/<uuid:pk>/activate', views.item_activate_view, name='item-activate'),

    # Game
    path('games/', views.GamesView.as_view(), name='game-list'),
    path('games/finished', views.FinishedGamesView.as_view(), name='game-finished'),
    path('game/new/', views.GameCreateView.as_view(), name='game-register'),
    path('game/<uuid:pk>', views.game_play, name='game-play'),
    path('game/<uuid:pk>/finished', views.GameDetailView.as_view(), name='game-detail')
]
