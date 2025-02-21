from django.contrib import admin

from store.models import Enterprise, Product


@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "level", "country", "city", "debt", "supplier")
    list_filter = ("city", "country",)
    actions = ('clear_debt',)

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "product_model", "release_date")
    list_filter = ("supplier", "release_date")
    search_fields = ("name", "supplier",)