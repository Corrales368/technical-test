# Import django
from django.contrib import admin

# From self app
from . import models

admin.site.register(models.Student)