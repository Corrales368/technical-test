# Import django
from django.contrib import admin

# Import self app
from apps.user.models import User

admin.site.register(User)
