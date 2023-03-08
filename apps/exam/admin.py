# Import django
from django.contrib import admin

# From self app
from . import models


class AnswerStudentModelAdmin(admin.ModelAdmin):
    """
    Custom class to override want and filter records by owned by each student
    """
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        new_queryset = queryset.filter(student=request.user.student)
        return new_queryset
    

admin.site.register(models.Exam)
admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.AnswerStudent, AnswerStudentModelAdmin)



    