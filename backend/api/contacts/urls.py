from django.urls            import path, include
from rest_framework         import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg               import openapi
from drf_yasg.views         import get_schema_view
from .views                 import ContactViewSet, LabelViewSet

# API 문서화 설정
schema_view = get_schema_view(
    openapi.Info(
        title="Contacts Documentation",
        default_version='v1',
        description="API documentation for Contacts.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'labels', LabelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='api1-schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='api1-schema-redoc'),
]
