from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers
from myapp.api import views
from rest_framework.urlpatterns import format_suffix_patterns

#REST API routes
router = routers.DefaultRouter()
#router.register(r'forumposts', views.ForumpostViewSet) #use this for viewset approach
router.register(r'tags', views.TagViewSet)
router.register(r'users', views.UserViewSet)

#REST API
urlpatterns = [
    url(r'^', include(router.urls)),

    #class-based view approach
    #url(r'^$', views.api_root), #needed if you use all class-based views and want them to show up in the landing page for the browsable api
    url(r'^forumposts/$', views.ForumpostList.as_view(), name='forumpost-list'),
    url(r'^forumposts/(?P<pk>[0-9]+)/$', views.ForumpostDetail.as_view(), name='forumpost-detail'),
]
