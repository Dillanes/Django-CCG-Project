"""MAIN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from usuarios.views import Login, Logout, UserToken

schema_view = get_schema_view(
   openapi.Info(
      title="C&C Group APIs",
      default_version='v1',
      description="Documentación de API de Consulting Construction",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jose.cano@consulting.construction"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('Login/', Login.as_view(), name = 'Login'),
    path('Logout/', Logout.as_view(), name = 'Logout'),
    path('refresh-token/',UserToken.as_view(), name = 'refresh_token'),
    path('apiUFT/', include('UNIFORMAT.urls')),
    path('apiOMC23/', include('OMNICLAS23.urls')),
    path('apiOMC41/', include('OMNICLAS41.urls')),
    path('apiOMC34/', include('OMNICLAS34.urls')),
    path('apiOMC35/', include('OMNICLAS35.urls')),
    path('apiMateriales/', include('MATERIALES.urls')),
    path('apiRolesOrg/', include('ROLESORG.urls')),
    path('apiUsuario/', include('usuarios.urls')),
    path('apiDatosGeograficos/', include('DATOSGEOGRAFICOS.urls')),
    path('apiProveedores/', include('PROVEEDORES.urls')),
]
