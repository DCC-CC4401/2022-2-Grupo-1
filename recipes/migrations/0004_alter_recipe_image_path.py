# Generated by Django 4.1.2 on 2022-10-10 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image_path',
            field=models.CharField(default='default.svg', max_length=255),
        ),
    ]