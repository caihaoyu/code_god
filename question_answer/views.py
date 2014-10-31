from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import generics, permissions
from question_answer.models import Question, Answer, Tag
from question_answer.serializers import QuestionListSerializer, QuestionSerializer, TagSerializer
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response


@login_required()
def list_question(request):
    return render_to_response('question/list.html', locals(), RequestContext(request))


class QuestionList(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    model = Question
    paginate_by = 5
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        # return Weekly.objects.get(issues__contains='1')
        return Question.objects.filter(title__contains=self.kwargs.get('title'))


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Question
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        answers = self.request.DATA["answers"]
        for i in range(len(answers)):
            if answers[i].get("id", 0) > 0:
                answer = Answer.objects.get(pk=answers[i]["id"])
                answer.content = answers[i]["content"]
                answer.is_accept = answers[i]["is_accept"]
                answer.original_author = answers[i]["original_author"]
                answer.save()
            else:
                answer = Answer(content=answers[i]["content"], is_accept=answers[i]["is_accept"],
                                original_author=answers[i]["original_author"],
                                questions=obj, author=self.request.user)
                answer.save()


class QuestionPost(generics.ListCreateAPIView):
    serializer_class = QuestionListSerializer
    model = Question
    paginate_by = 5
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        if self.request.DATA["content"] and self.request.DATA["original_author"]:
            obj.content = self.request.DATA["content"]
            obj.original_author = self.request.DATA["original_author"]
        else:
            obj.content = ""
        obj.author = self.request.user

    def post_save(self, obj, created=True):
        if self.request.DATA["answers"]:
            answers = self.request.DATA["answers"]
            for i in range(len(answers)):
                answer = Answer(content=answers[i]["content"], is_accept=answers[i]["is_accept"],
                                original_author=answers[i]["original_author"],
                                questions=obj, author=self.request.user)
                answer.save()


class TagPost(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    model = Tag
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA, files=request.FILES)

        if serializer.is_valid():
            self.pre_save(serializer.object)
            try:
                tag = Tag.objects.get(title=serializer.object.title)
                self.object = tag
            except Exception as ex:
                self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            serializer = TagSerializer(self.object)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagSearch(generics.ListAPIView):
    serializer_class = TagSerializer
    model = Tag
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        # return Weekly.objects.get(issues__contains='1')
        list = self.request.GET.getlist("list")
        ids = []
        if list is not None:
            for tag in list:
                ids.append(int(tag))

        return Tag.objects.filter(title__contains=self.kwargs.get('title')).exclude(id__in=ids)