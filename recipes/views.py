from django import shortcuts
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

from . import models

class LecturaRecetaView(generic.TemplateView):
    """
    Recipe Reading View class.
    
    Handles the view's requests.
    """

    def get(self, request, id_recipe):
        """
        Manage a get request.
        
        Returns:
            A rendered view with the recipe template.
        """

        try:
            recipe = models.Recipe.objects.get(id=id_recipe)
        except models.Recipe.DoesNotExist:
            return shortcuts.render(request, "display.html")

        view_context = {
            "recipe": recipe
        }

        return shortcuts.render(request, "recipe.html", context=view_context)


class RecetasView(generic.TemplateView):
    """
    Recipes Dispay View class.
    
    Handles the view's requests.
    """

    def get(self, request):
        """
        Manage a get request.
        
        Returns:
            A rendered view with the recipes dispay.
        """

        recipes_list = models.Recipe.objects.all()

        view_context = {
            "recipes": recipes_list
        }

        return shortcuts.render(request, "recipe.html", context=view_context)