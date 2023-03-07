# Import django
from django.contrib import admin

# From self app
from . import models

admin.site.register(models.Exam)
admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.AnswerStudent)