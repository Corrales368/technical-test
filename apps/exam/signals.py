# Import django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Import self app
from .models import Answer, AnswerStudent


@receiver(post_save, sender=Answer)
def update_answer_student(sender, instance, **kwargs):
    """
    Signal to update AnswerStudent objects when an Answer object is updated
    """
    answer_students = AnswerStudent.objects.filter(answer=instance)
    for answer_student in answer_students:
        answer_student.is_correct = instance.is_correct
        answer_student.save()
