from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^mine/$', MyView.as_view(), name='my_view'),
    url(r'^$', UsersListView.as_view(), name='users_list'),
    url(r'^$', AboutApp.as_view(), name='about'),
]