from django.shortcuts import render
from django.views import generic
from django import shortcuts

class HomepageView(generic.TemplateView):
    """
    Homepage View class.
    
    Handles the homepage requests.
    """

    def get(self, request):
        """
        Manage a get request.
        
        Returns:
            A rendered view with the homepage template.
        """

        view_context = {
            "var1": 1,
            "var2": 2
        }
        return shortcuts.render(request, "index.html", context=view_context)


class LecturaRecetaView(generic.TemplateView):
    """
    Recipe Reading View class.
    
    Handles the view's requests.
    """

    def get(self, request):
        """
        Manage a get request.
        
        Returns:
            A rendered view with the recipe template.
        """

        view_context = {

        }

        return shortcuts.render(request, "recipe.html", context=view_context)