from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import auth
from weekly.form import LoginForm
from weekly.models import Weekly, Article, OrderShip
from rest_framework import generics, permissions
from weekly.serializers import WeeklySerializer, ArticleSerializer

# Create your views here.


def home(request):
    return render_to_response('weekly/home.html', locals(), RequestContext(request))


def login(request):
    if request.method == 'GET':
        next = request.GET.get('next')
        return render_to_response('weekly/login.html', locals(), RequestContext(request))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            next = request.POST.get('next')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(next)
            else:
                return render_to_response('weekly/login.html',
                                          RequestContext(request, {'form': form, 'if_login': True, 'next': next}))
        else:
            return render_to_response('weekly/login.html', RequestContext(request, {'form': form}))


def list_weekly(request):
    return render_to_response('weekly/list.html', locals(), RequestContext(request))


class WeekList(generics.ListCreateAPIView):
    model = Weekly
    serializer_class = WeeklySerializer
    paginate_by = 5
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post_save(self, obj, created=False):
        articles = self.request.DATA['articles']
        change_articles(obj, articles)


# def pre_save(self, obj):
# obj.owner = self.request.user


class WeekPostList(generics.ListAPIView):
    model = Weekly
    serializer_class = WeeklySerializer
    paginate_by = 5
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        # return Weekly.objects.get(issues__contains='1')
        return Weekly.objects.filter(issues__contains=self.kwargs.get('issues'))


class ArticleList(generics.ListCreateAPIView):
    model = Article
    serializer_class = ArticleSerializer
    paginate_by = 5
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class WeeklyDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Weekly
    serializer_class = WeeklySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        articles = self.request.DATA['articles']
        change_articles(obj, articles)


def change_articles(weekly, articles):
    weekly.article_set.clear()
    print(articles)
    for i in range(len(articles)):
        try:
            article = Article.objects.get(id=articles[i]['id'])

            order = OrderShip(weekly=weekly, article=article, number=i)
            order.save()
        except Exception as ex:
            print(ex)



