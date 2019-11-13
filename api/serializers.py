from rest_framework import serializers

from . import models
from pprint import pprint

class PizzaFlavorSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = models.PizzaFlavor
        fields = "__all__"

    def to_representation(self, value):
        return value.name

class PizzaFlavorField(serializers.RelatedField):
    def to_internal_value(self, name):
        value = models.PizzaFlavor.objects.get(name=name)
        return value
    def to_representation(self, value):
        return value.name


class OrderedPizzaSerializer(serializers.HyperlinkedModelSerializer):
    pizza_flavor = PizzaFlavorField(queryset=models.PizzaFlavor.objects.all())

    class Meta:
        model = models.OrderedPizza
        fields = ["url", "pizza_flavor", "count", "size"]
        read_only_fields = ('pizza_flavor',)


class DeliveryDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.DeliveryDetail
        fields = "__all__"


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    ordered_pizzas = OrderedPizzaSerializer(many=True, required=False)
    delivery_detail = DeliveryDetailSerializer(required=False)

    class Meta:
        model = models.Order
        fields =["url",  "customer_id", "is_paid", "ordered_pizzas", "delivery_detail"]

    def create(self, validated_data):
        ordered_pizzas = validated_data.pop('ordered_pizzas')
        order = models.Order.objects.create(
            delivery_detail = models.DeliveryDetail.objects.create(),
            **validated_data
        )
        for ordered_pizza_details in ordered_pizzas:
            ordered_pizza_details = dict(ordered_pizza_details)
            ordered_pizza = models.OrderedPizza.objects.create(
                    **ordered_pizza_details
                )
            order.ordered_pizzas.add(
                ordered_pizza
            )
        order.save()
        return order

