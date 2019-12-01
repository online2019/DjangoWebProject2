"""
Definition of urls for DjangoWebProject2.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib.auth.views import  LoginView, LogoutView

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

#from django_summernote.views import (
#    SummernoteEditor, SummernoteUploadAttachment)


urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^blog$', app.views.blog, name='blog'),
    url(r'^(?P<parametr>\d+)/$', app.views.blogpost, name='blogpost'),

    url(r'^links$', app.views.links, name='links'),
    url(r'^newpost$', app.views.newpost, name='newpost'),
    url(r'^videopost$', app.views.videopost, name='videopost'),

    url(r'^registration$', app.views.registration, name='registration'),
    
    
    
    
    
    
    
    
    
    
    #url(r'^login/$',
    #    django.contrib.auth.views.login,
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': app.forms.BootstrapAuthenticationForm,
    #        'extra_context':
    #        {
    #            'title': 'Вход',
    #            'year': datetime.now().year,
    #        }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    django.contrib.auth.views.logout,
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),

    url('login/', LoginView.as_view(template_name='app/login.html', authentication_form=app.forms.BootstrapAuthenticationForm), name='login'), 
    url('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^editor/(?P<id>.+)/$', SummernoteEditor.as_view(),
    #    name='django_summernote-editor'),
    #url(r'^upload_attachment/$', SummernoteUploadAttachment.as_view(),
    #    name='django_summernote-upload_attachment'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
