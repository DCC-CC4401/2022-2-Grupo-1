from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return (f"User("
                f"username={self.username}, "
                f"name={self.first_name} {self.last_name}, "
                f"email={self.email}"
                f")")


class Recipe(models.Model):
    # Llave foránea del usuario que escribe la receta
    user_id = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    # Nombre de la receta
    name = models.CharField(max_length=255)
    # Ingredientes
    ingredients = models.TextField()
    # Instrucciones de la preparación
    instructions = models.TextField()
    # Path de la imagen linkeada
    image_path = models.CharField(max_length=255)

    def __str__(self):
        return (f"Recipe("
                f"id={self.id}, "
                f"user_id={self.user_id}, "
                f"name={self.name}"
                f")")
