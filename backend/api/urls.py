from django.urls import path
from django.conf.urls import url
from rest_framework.authtoken import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    url(r'^auth/$', auth_views.obtain_auth_token),
    url(r'^signup/$', views.SignupView.as_view()),
    url(r'^attendance/$', views.AttendanceCreateDestroyView.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentView.as_view()),
    url(r'^events_list/$', views.EventListView.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventView.as_view()),
    url(r'^follow/$', views.FollowView.as_view()),
    url(r'^medias/(?P<pk>[0-9]+)/$', views.MediaView.as_view()),
    url(r'^tags/$', views.TagList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserView.as_view()),
    url(r'^vote/$', views.VoteView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
