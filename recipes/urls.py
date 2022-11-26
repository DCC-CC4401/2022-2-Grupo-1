from django.urls import path

from . import views

urlpatterns = [
    path('', views.RecetasView.as_view(), name="recipes"),
    path('<int:id_recipe>/', views.LecturaRecetaView.as_view(), name="recipe"),
    path('new/', views.NewRecipeView.as_view(), name="new-recipe"),
    path('edit/<int:id_recipe>/', views.EditRecipeView.as_view(), name="edit-recipe"),
    path('search', views.SearchRecipesView.as_view(), name="search-result"),
]
