# Import django
from rest_framework import serializers

# Import self app
from apps.exam.models import Exam, Question, Answer, AnswerStudent


class ExamSerializer(serializers.ModelSerializer):
    """
    Serializer for the exam model class
    """
    class Meta:
        model = Exam
        fields = [
            'id',
            'name',
            'description',
        ]

class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for the question model class
    """
    class Meta:
        model = Question
        fields = [
            'id',
            'text',
            'exam',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['exam'] = instance.exam.__str__()
        return representation


class AnswerSerializer(serializers.ModelSerializer):
    """
    Serializer for the answer model class
    """
    class Meta:
        model =  Answer
        fields = [
            'id',
            'text',
            'question',
            'is_correct',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['question'] = instance.question.__str__()
        return representation


class AnswerStudentSerializer(serializers.ModelSerializer):
    """
    Serializer for the answer of student model class
    """    
    class Meta:
        model = AnswerStudent
        fields = [
            'question',
            'answer',
            'student',
            'is_correct',
        ]
        read_only_fields  = [
            'is_correct',
        ]
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['question'] = instance.question.__str__()
        representation['answer'] = instance.answer.__str__()
        representation['student'] = instance.student.__str__()
        return representation 
