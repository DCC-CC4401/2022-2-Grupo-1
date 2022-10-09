from django.shortcuts import render
from django.views import generic
from django import shortcuts

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


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

class LoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('homepage')

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('homepage')
        return super(RegisterView, self).get(*args, **kwargs)
