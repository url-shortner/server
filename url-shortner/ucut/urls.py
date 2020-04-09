"""airtxt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="ucut api 입니다.",
        default_version='v1',
        description="ucut api입니다.",
        terms_of_service="",
        contact=openapi.Contact(email="contact@among.software"),
        license=openapi.License(name="Copyright ⓒ 2019, Among Co.,Ltd"),
    ),
    public=False,
)
urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('', include('shorturl.urls')),
    path('accounts/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', login_required(schema_view.without_ui(cache_timeout=0)),
            name='schema-json'),
    re_path(r'^swagger/$', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    re_path(r'^redoc/$', login_required(schema_view.with_ui('redoc', cache_timeout=0)), name='schema-redoc'),
]
