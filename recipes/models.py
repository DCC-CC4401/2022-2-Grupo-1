from django.db import models

# Create your models here.
from webpage.models import User


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
