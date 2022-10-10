from django.contrib.auth.forms import UserCreationForm

from webpage.models import User


class AdapterUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
