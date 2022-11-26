from django import shortcuts
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views import generic

import PIL

from . import forms
from . import models


class LecturaRecetaView(generic.TemplateView):
    """
    Recipe Reading View class.
    
    Handles the view's requests.
    """

    # noinspection PyMethodOverriding
    def get(self, request, recipe_id):
        """
        Manage a get request.
        
        Returns:
            A rendered view with the recipe template.
        """

        try:
            recipe = models.Recipe.objects.get(id=recipe_id)
        except models.Recipe.DoesNotExist:
            return shortcuts.render(request, "display.html")



        view_context = {
            "recipe": recipe
        }

        if request.user.is_authenticated:
            view_context["is_saved"] = models.UserLikesRecipe.objects.filter(user=request.user, recipe=recipe).exists()

        return shortcuts.render(request, "recipe.html", context=view_context)

    def post(self, request, recipe_id):
        try:
            recipe = models.Recipe.objects.get(id=recipe_id)
        except models.Recipe.DoesNotExist:
            return shortcuts.render(request, "display.html")

        save = request.POST["saved"] == "true"
        if save:
            like, created = models.UserLikesRecipe.objects.get_or_create(user=request.user, recipe=recipe)
            like.save()
        else:
            like = models.UserLikesRecipe.objects.get(user=request.user, recipe=recipe)
            like.delete()

        try:
            recipe = models.Recipe.objects.get(id=recipe_id)
        except models.Recipe.DoesNotExist:
            return shortcuts.render(request, "display.html")

        view_context = {
            "recipe": recipe,
            "is_saved": models.UserLikesRecipe.objects.filter(user=request.user, recipe=recipe).exists()
        }

        return shortcuts.render(request, "recipe.html", context=view_context)


class RecetasView(generic.TemplateView):
    """
    Recipes Display View class.
    
    Handles the view's requests.
    """

    # noinspection PyMethodOverriding
    def get(self, request):
        """
        Manage a get request.
        
        Returns:
            A rendered view with the recipes display.
        """

        recipes_list = models.Recipe.objects.all()

        view_context = {
            "recipes": recipes_list
        }

        return shortcuts.render(request, "display.html", context=view_context)

class RecetasCreadasView(generic.TemplateView):
    """
    Own recipes Display View class.

    Handles the view's requests.
    """

    # noinspection PyMethodOverriding
    def get(self, request):
        """
        Manage a get request.

        Returns:
            A rendered view with the recipes display.
        """

        recipes_list = models.Recipe.objects.filter(user=request.user)

        view_context = {
            "recipes": recipes_list
        }

        return shortcuts.render(request, "display.html", context=view_context)

class RecetasGuardadasView(generic.TemplateView):
    """
    Saved recipes Display View class.

    Handles the view's requests.
    """

    # noinspection PyMethodOverriding
    def get(self, request):
        """
        Manage a get request.

        Returns:
            A rendered view with the recipes display.
        """

        recipes_list = [x.recipe for x in models.UserLikesRecipe.objects.filter(user=request.user)]

        view_context = {
            "recipes": recipes_list
        }

        return shortcuts.render(request, "display.html", context=view_context)


class NewRecipeView(generic.TemplateView):
    """
    New Recipe View class.

    Handles the view's requests.
    """

    # noinspection PyMethodOverriding
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

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        """
        Manage the form submit.

        Returns:
            A rendered view with the created recipe.
        """

        recipe_data = forms.NewRecipeForm(request.POST, request.FILES)

        if recipe_data.is_valid():
            recipe_data = recipe_data.cleaned_data
            recipe = models.Recipe(
                user=request.user,
                name=recipe_data["name"],
                ingredients=recipe_data["ingredients"],
                instructions=recipe_data["instructions"],
                image = recipe_data["image"]
            )

            recipe.save()

            return HttpResponseRedirect(f"/recipes/{recipe.id}")

        return HttpResponseRedirect("/recipes/new/")


class EditRecipeView(generic.TemplateView):
    """
    Edit Recipe View class.

    Handles the view's requests.
    """

    # noinspection PyMethodOverriding
    def get(self, request, recipe_id):
        """
        Manage a get request.

        Returns:
            A rendered view with the edit recipe form.
        """

        try:
            recipe = models.Recipe.objects.get(id=recipe_id)
        except models.Recipe.DoesNotExist:
            return HttpResponseRedirect(f"/recipes/{recipe_id}")

        if request.user != recipe.user:
            return HttpResponseRedirect(f"/recipes/{recipe_id}")

        recipe_form = forms.NewRecipeForm(instance=recipe)

        view_context = {
            "form": recipe_form,
            "recipe_id": recipe_id,
        }

        return shortcuts.render(request, "edit.html", context=view_context)

    # noinspection PyMethodMayBeStatic
    def post(self, request, recipe_id):
        """
        Manage the form submit.

        Returns:
            A rendered view with the created recipe.
        """

        recipe_data = forms.NewRecipeForm(request.POST, request.FILES)
        recipe = models.Recipe.objects.get(id=recipe_id)
        if recipe_data.is_valid():
            recipe_data = recipe_data.cleaned_data

            recipe.user=request.user
            recipe.name=recipe_data["name"]
            recipe.ingredients=recipe_data["ingredients"]
            recipe.instructions=recipe_data["instructions"]
            recipe.image=recipe_data["image"]

            recipe.save()

            return HttpResponseRedirect(f"/recipes/{recipe.id}")

        return HttpResponseRedirect(f"/recipes/edit/{recipe.id}")


class SearchRecipesView(generic.ListView):
    model = models.Recipe
    template_name = 'search_results.html'
    ...
