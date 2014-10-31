from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from weekly.views import WeekList,ArticleList,WeeklyDetail,WeekPostList
from question_answer.views import QuestionList,QuestionPost,QuestionDetail,TagPost,TagSearch
from django.conf.urls.static import static

admin.autodiscover()
weekly_urls = patterns('',
    url(r'^$', WeekList.as_view(), name='weekly-list'),
    url(r'^/(?P<pk>\d+)$', WeeklyDetail.as_view(), name='weekly-detail'),
    url(r'^/search/(?P<issues>[0-9a-zA-Z_-]+)$', WeekPostList.as_view(), name='weekly-list')
)
article_urls=patterns('',
    url(r'^$', ArticleList.as_view(), name='article-list'),
)
question_urls=patterns('',
    url(r'^$', QuestionPost.as_view(), name='question-list'),
    url(r'^/(?P<pk>\d+)$', QuestionDetail.as_view(), name='question-detail'),
    url(r'^/search/(?P<title>.+)$', QuestionList.as_view(), name='question-list')
)
tag_urls=patterns('',
    url(r'^$', TagPost.as_view(), name='tag-list'),
    url(r'^/search/(?P<title>.+)$', TagSearch.as_view(), name='tag-search'),
)


urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'question_answer.views.list_question', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^home', 'question_answer.views.list_question', name='home'),
                       url(r'^weekly/home', 'weekly.views.home', name='home'),
                       # url(r'^jobs/(?P<job_id>\d+)/$', 'jobs.views.detail'),
                       url(r'^data/(?P<path>.*)$', 'django.views.static.serve', {
                           'document_root': settings.MEDIA_ROOT,
                       }),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
                           'document_root': settings.STATIC_ROOT,
                       }),
                       (r'^accounts/login/$', 'weekly.views.login'),
                       (r'^weekly/list/$', 'weekly.views.list_weekly'),
                       (r'^question/list/$', 'question_answer.views.list_question'),
                       url(r'^api/weekly', include(weekly_urls)),
                       url(r'^api/article', include(article_urls)),
                       url(r'^api/question', include(question_urls)),
                       url(r'^api/tag', include(tag_urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


)
