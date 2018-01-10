from django.conf.urls import url, include
from . import views




urlpatterns = [
    url(r'^$', views.FinanceHomeView.as_view()),
    url(r'^(?:people|companies|committees)/(?P<id>[\w-]+)/$', views.EntityDetailView.as_view(), name='finance_entity'),
    url(r'^(?:people|companies|committees)/(?P<id>[\w-]+)/spending$', views.EntityDetailSpendingListView.as_view(),
        name='finance_entity_sp_list'),
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]