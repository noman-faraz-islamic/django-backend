# serializers.py
from rest_framework import serializers
from .models import Question, Option

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'option_text', 'question']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    right_option = OptionSerializer(read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'right_option', 'options']
