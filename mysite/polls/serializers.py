from rest_framework import serializers

from .models import Question, Choice

'''class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date')'''

'''class ChoiceSerializer(serializers.ModelSerializer):
    choice = QuestionSerializer(read_only=True)

    class Meta:
        model = Choice
        fields = ('__all__')'''



class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('__all__')

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']
