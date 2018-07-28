from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PersonView, name='index'),
    url(r'^if/$', views.hello_if, name='hello_if'), # 追加する
    url(r'^for/$', views.hello_for, name='hello_for'),
    url(r'^get/$', views.hello_get_query, name='hello_get_query'),
    url(r'^forms/$', views.hello_forms, name='hello_forms'),
    url(r'^forms_second/$', views.hello_forms_second, name='hello_forms_second'),
]
