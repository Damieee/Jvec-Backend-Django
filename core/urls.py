from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Ezekiel Oluwadamilare's Solution for JVEC ASSESSMENT BACKEND (django)",
        default_version='v1',
        description="This is the Swagger Documentation of Jvec Internship Backend Test",
        contact=openapi.Contact(email="ezekieloluwadamy@gmail.com"),
        license=openapi.License(name="None"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authentication/', include('api.authentication.urls')),
    path('api/contacts/', include('api.contacts.urls')),
    path("swagger<str:format>", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    ]


