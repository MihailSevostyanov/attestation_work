from rest_framework.serializers import ModelSerializer

from store.models import Enterprise, Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class EnterpriseSerializer(ModelSerializer):

    class Meta:
        model = Enterprise
        fields = "__all__"