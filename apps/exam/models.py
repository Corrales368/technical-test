# Import django
from django.db import models

# Import shared app
from apps.shared.constants import ConstantsCharFields

# Import project apps
from apps.student.models import Student


class Exam(models.Model):
    """
    Model to store exams
    """
    name = models.CharField(max_length=ConstantsCharFields.MAX_LENGTH_MEDIUM)
    description = models.CharField(max_length=ConstantsCharFields.MAX_LENGTH_EXTRA_LARGE)
    
    def __str__(self) -> str:
        return self.name
    

class Question(models.Model):
    """
    Model to store questions
    """
    text = models.CharField(max_length=ConstantsCharFields.MAX_LENGTH_LARGE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text
    

class Answer(models.Model):
    """
    Model to store answer
    """
    text = models.CharField(max_length=ConstantsCharFields.MAX_LENGTH_MEDIUM)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text
    

class AnswerStudent(models.Model):
    """
    Model to store answers of students
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    class Meta:
        constraints = [
            # a student can only have one answer for each question
            models.UniqueConstraint(fields=['student', 'question'],name='unique_student_question')
        ]
    
    def save(self, *args, **kwargs):
        self.is_correct = self.answer.is_correct
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.question} {self.is_correct}'
    


    