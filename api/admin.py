from django.contrib import admin
from django import forms

from . import models


class PizzaFlavorAdminForm(forms.ModelForm):

    class Meta:
        model = models.PizzaFlavor
        fields = "__all__"


class PizzaFlavorAdmin(admin.ModelAdmin):
    form = PizzaFlavorAdminForm
    list_display = [
        "id",
        "name",
        "s_size_price",
        "m_size_price",
        "l_size_price",
    ]
    readonly_fields = [
        "m_size_price",
        "s_size_price",
        "l_size_price",
        "id",
        "name",
    ]


class OrderedPizzaAdminForm(forms.ModelForm):

    class Meta:
        model = models.OrderedPizza
        fields = "__all__"


class OrderedPizzaAdmin(admin.ModelAdmin):
    form = OrderedPizzaAdminForm
    list_display = [
        "id",
        "size",
        "created",
        "count",
    ]
    readonly_fields = [
        "id",
        "size",
        "created",
        "count",
    ]


class OrderAdminForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = "__all__"


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = [
        "id",
        "customer_id",
        "last_updated",
        "created",
        "is_paid",
    ]
    readonly_fields = [
        "customer_id",
        "last_updated",
        "created",
        "is_paid",
        "id",
    ]


class DeliveryDetailAdminForm(forms.ModelForm):

    class Meta:
        model = models.DeliveryDetail
        fields = "__all__"


class DeliveryDetailAdmin(admin.ModelAdmin):
    form = DeliveryDetailAdminForm
    list_display = [
        "id",
        "assigned_courier_id",
        "status",
        "created",
    ]
    readonly_fields = [
        "assigned_courier_id",
        "status",
        "id",
        "created",
    ]


admin.site.register(models.PizzaFlavor, PizzaFlavorAdmin)
admin.site.register(models.OrderedPizza, OrderedPizzaAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.DeliveryDetail, DeliveryDetailAdmin)