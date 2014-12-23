from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from board import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/',include('django_markdown.urls')),
    url(r'^',include('board.urls')),

)

urlpatterns += static('static_files', document_root=settings.MEDIA_ROOT)