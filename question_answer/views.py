from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import generics, permissions
from question_answer.models import Question,Answer,Tag
from question_answer.serializers import QuestionListSerializer,QuestionSerializer
from django.contrib.auth.decorators import login_required


@login_required()
def list_question(request):
    return render_to_response('question/list.html', locals(), RequestContext(request))


class QuestionList(generics.ListAPIView):
    serializer_class =QuestionListSerializer
    model = Question
    paginate_by = 20
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Question
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class QuestionPost(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    model = Question
    paginate_by = 5
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.author = self.request.user