__author__ = 'chy'
from rest_framework import serializers
from weekly.models import Weekly, Article
# -*- coding: utf-8 -*-
class WeeklySerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.Field(source='get_articles_rest')
    # articles = ArticleSerializer(many=True)
    class Meta:
        model = Weekly
        fields = ('id','issues', 'create_date', 'send_date', 'is_send','articles')


class ArticleDetailSerializer(serializers.HyperlinkedModelSerializer):
    weeklys = serializers.PrimaryKeyRelatedField(many=True)
    # ids=[]
    class Meta:
        model = Article
        fields = ('id','title', 'article_content', 'create_date', 'edit_date', 'weeklys', 'order')

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    # ids=[]
    class Meta:
        model = Article
        fields = ('id','title',  'create_date', 'edit_date',  'order')