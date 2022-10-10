from django import shortcuts
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponseForbidden, HttpResponseRedirect

from . import models
from . import forms

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

    def post(self, request, id_recipe):
        return self.get(request, id_recipe)


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

        
class NewRecipeView(generic.TemplateView):
    """
    New Recipe View class.
    
    Handles the view's requests.
    """

    def get(self, request):
        """
        Manage a get request.
        
        Returns:
            A rendered view with the new recipe form.
        """

        recipe_form = forms.NewRecipeForm()

        view_context = {
            "form": recipe_form
        }

        return shortcuts.render(request, "new.html", context=view_context)


    def post(self, request):
        """
        Manage the form submit.
        
        Returns:
            A rendered view with the created recipe.
        """

        recipe_data = forms.NewRecipeForm(request.POST, request.FILES)

        if recipe_data.is_valid():
            try:
                img = request.FILES["image"]
                image_path = img.name

                with open(f"recipes/static/img/uploads/{img.name}", "wb+") as destination:
                    for chunk in img.chunks():
                        destination.write(chunk)

            except MultiValueDictKeyError:
                image_path = models.Recipe._meta.get_field("image_path").get_default()

            recipe_data = recipe_data.cleaned_data
            recipe = models.Recipe(user=request.user, name=recipe_data["name"], ingredients=recipe_data["ingredients"], instructions=recipe_data["instructions"], image_path=image_path)
            recipe.save()

            return HttpResponseRedirect(f"/recipes/{recipe.id}")

        return HttpResponseRedirect("/recipes/new/")