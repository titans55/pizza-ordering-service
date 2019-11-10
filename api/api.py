from rest_framework import viewsets
from . import serializers
from . import models


class PizzaFlavorViewSet(viewsets.ModelViewSet):
    """ViewSet for the PizzaFlavor class"""

    queryset = models.PizzaFlavor.objects.all()
    serializer_class = serializers.PizzaFlavorSerializer
    filterset_fields = (
        '__all__'
    )


class OrderedPizzaViewSet(viewsets.ModelViewSet):
    """ViewSet for the OrderedPizza class"""

    queryset = models.OrderedPizza.objects.all()
    serializer_class = serializers.OrderedPizzaSerializer
    filterset_fields = (
        '__all__'
    )


class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet for the Order class"""

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    filterset_fields = (
        'is_paid',
        'delivery_detail__status',
        'customer_id',
        'created',
    )


class DeliveryDetailViewSet(viewsets.ModelViewSet):
    """ViewSet for the DeliveryDetail class"""

    queryset = models.DeliveryDetail.objects.all()
    serializer_class = serializers.DeliveryDetailSerializer
