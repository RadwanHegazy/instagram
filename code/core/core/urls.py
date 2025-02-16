"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view for Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Instagram API Docs",
        default_version='v1',
        description="A clear description for each endpoint on the system.",
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('users.apis.urls')),
    path('api/v1/posts/', include('posts.apis.urls')),
    path('api/v1/story/', include('story.apis.urls')),
    path('api/v1/chat/', include('chat.apis.urls')),
    path('api/v1/notifications/', include('notifications.apis.urls')),   

    path('__docs__/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
