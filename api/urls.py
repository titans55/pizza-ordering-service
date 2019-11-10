
from django.urls import path, include
from rest_framework import routers
from PizzaOrderingService import settings
from . import api


router = routers.DefaultRouter()
router.register("PizzaFlavor", api.PizzaFlavorViewSet)
router.register("OrderedPizza", api.OrderedPizzaViewSet)
router.register("Order", api.OrderViewSet)
router.register("DeliveryDetail", api.DeliveryDetailViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]