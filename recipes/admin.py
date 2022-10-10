from django.contrib import admin

import recipes.models

admin.site.register(recipes.models.Recipe)
