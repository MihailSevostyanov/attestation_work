from django.urls import path

from store.apps import StoreConfig
from store.views import EnterpriseListAPIView, EnterpriseCreateAPIView, \
    EnterpriseDestroyAPIView, EnterpriseUpdateAPIView, \
    EnterpriseRetrieveAPIView, ProductListAPIView, ProductCreateAPIView, \
    ProductRetrieveAPIView, ProductUpdateAPIView, ProductDestroyAPIView

app_name = StoreConfig.name

urlpatterns = [
    path("enterprise/", EnterpriseListAPIView.as_view(), name="enterprise_list"),
    path("enterprise/create/", EnterpriseCreateAPIView.as_view(), name="enterprise_create"),
    path("enterprise/<int:pk>/", EnterpriseRetrieveAPIView.as_view(), name="enterprise_retrieve"),
    path("enterprise/<int:pk>/update/", EnterpriseUpdateAPIView.as_view(), name="enterprise_update"),
    path("enterprise/<int:pk>/delete/", EnterpriseDestroyAPIView.as_view(), name="enterprise_delete"),

    path("product/", ProductListAPIView.as_view(), name="product_list"),
    path("product/create/", ProductCreateAPIView.as_view(), name="eproduct_create"),
    path("product/<int:pk>/", ProductRetrieveAPIView.as_view(), name="product_retrieve"),
    path("product/<int:pk>/update/", ProductUpdateAPIView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDestroyAPIView.as_view(), name="product_delete"),
]