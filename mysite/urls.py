from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},name="logout"),
    url(r'', include('blog.urls')),
]
