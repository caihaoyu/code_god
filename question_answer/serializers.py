__author__ = 'chy'
from rest_framework import serializers
from question_answer.models import Question, Answer, Tag
# -*- coding: utf-8 -*-


class QuestionListSerializer(serializers.HyperlinkedModelSerializer):
    answers_count = serializers.Field(source='get_answer_count')

    class Meta:
        model = Question
        fields = ('id', 'title', 'trackback_url', 'answers_count')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = serializers.Field(source='get_answer_rest')
    author = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Question
        fields = ('id', 'title', 'trackback_url', 'author', 'content', 'original_author', 'create_date', 'edit_date', 'answers')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer