
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include, re_path
from apps.posts.urls import urlpatterns as ur
from config import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.posts.urls')),
    path('captcha/',include('captcha.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path("__debug__/", include("debug_toolbar.urls")),] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
