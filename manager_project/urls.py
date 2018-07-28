"""manager_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

import manager.views as manager_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', manager_view.CustomLoginView.as_view()),
    url(r'^logout/', manager_view.logout_view),
    url(r'^worker_list/', login_required(manager_view.WorkerListView.as_view())),
    url(r'^manager_inf/', include(('manager.urls','manager'),)),
#    url(r'^hijack/', include('hijack.urls')),
    url(r'^crud/', include(('crud.urls','crud'),)),  # 追加する
    url(r'^guestboard/', include(('guestboard.urls','guestboard'),)), 
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
