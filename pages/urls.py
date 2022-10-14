from django.urls import re_path as url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.button),
    url(r'^output', views.output,name="script"),
]


