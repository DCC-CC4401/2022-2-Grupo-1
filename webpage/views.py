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

        return shortcuts.render(request, "homepage/index.html")