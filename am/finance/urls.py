from django.conf.urls import url, include
from . import views




urlpatterns = [
    url(r'^(?:people|companies|committees)/(?P<id>[\w-]+)/$', views.EntityDetailView.as_view(), name='finance_entity'),
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]