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

        context = {
            "var1": 1,
            "var2": 2
        }
        return shortcuts.render(request, "index.html", context=context)