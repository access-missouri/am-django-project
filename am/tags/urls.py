from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.TagDetailView.as_view(), name='tag_detail'),
]