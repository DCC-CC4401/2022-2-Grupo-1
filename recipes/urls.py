from django.contrib import admin
from django.urls import path, include

from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.RecetasView.as_view(), name="recipes"),
    path('created-recipes/', views.RecetasCreadasView.as_view(), name="created-recipes"),
    path('saved-recipes/', views.RecetasGuardadasView.as_view(), name="saved-recipes"),
    path('<int:recipe_id>/', views.LecturaRecetaView.as_view(), name="recipe"),
    path('new/', views.NewRecipeView.as_view(), name="new-recipe"),
    path('edit/<int:recipe_id>/', views.EditRecipeView.as_view(), name="edit-recipe")
]
