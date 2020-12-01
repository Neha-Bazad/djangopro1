from rest_framework import serializers

from .models import Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('__all__')

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']
