from django.conf.urls import url, include
from . import views




urlpatterns = [
    url(r'^districts/(?P<id>[\w-]+)/$', views.DistrictDetailView.as_view(),
        name='district_detail'),
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]