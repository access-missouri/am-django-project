from django.conf.urls import url, include
from . import views




urlpatterns = [
    url(r'^sessions/(?P<id>[\w-]+)/$', views.LegislativeSessionView.as_view(), name='legislative_session'),
    url(r'^sessions$', views.LegislativeSessionListView.as_view(), name='legislative_session_list'),
    url(r'^sessions/memberships/(?P<id>[\w-]+)/$', views.BodyMembershipView.as_view(), name='body_membership'),
    # url(r'^(?:people|companies|committees)/(?P<id>[\w-]+)/spending$', views.EntityDetailSpendingListView.as_view(),
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]