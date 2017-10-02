"""blog URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from pro import views as pro_views
from contact import views as contact_views
from checkout import views as checkout_views
from posts import views as posts_views


from accounts.views import (login_view, register_view, logout_view)


urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include("comments.urls", namespace='comments')),
    url(r'^$', pro_views.home, name='home'),
    url(r'^about$', pro_views.about, name='about'),
    url(r'^profile$', pro_views.userProfile, name='profile'),
    url(r'^checkout$', checkout_views.checkout, name='checkout'),
    url(r'^contact$', contact_views.contact, name='contact'),
    url(r'^post_list', posts_views.post_list, name='post_list'),
    url(r'^post_create', posts_views.post_create, name='post_create'),

    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^posts/', include("posts.urls", namespace='posts')),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)