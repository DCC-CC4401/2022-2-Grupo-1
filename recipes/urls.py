from django.contrib import admin
from django.urls import path, include

from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.RecetasView.as_view(), name="recipes"),
    path('<int:id_recipe>/', views.LecturaRecetaView.as_view(), name="recipe"),
    path('new/', views.NewRecipeView.as_view(), name="new-recipe"),
    path('edit/<int:id_recipe>/', views.EditRecipeView.as_view(), name="edit-recipe")
]
