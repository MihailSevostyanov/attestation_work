from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView, \
    SpectacularAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', include('store.urls', namespace='store')),
    # path('users/', include('users.urls', namespace='users')),

    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
