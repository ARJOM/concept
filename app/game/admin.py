from django.contrib import admin
from .models import Item, Concept, Game


admin.site.register((Item, Concept, Game))
