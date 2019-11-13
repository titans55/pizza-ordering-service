from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Order

class OrderingPizzaSericeTest(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.orders_endpoint = "/api/v1/Order/"
        first_order_response = self.client.post(
            self.orders_endpoint, 
            {
                "customer_id": 2,
                "is_paid": False,
                "ordered_pizzas": [
                    {
                        "count": 4,
                        "size": "s",
                        "pizza_flavor": "Pepperoni"
                    },
                    {
                        "count": 1,
                        "size": "m",
                        "pizza_flavor": "Margarita"
                    }
                ]
            },
            format='json'
        )
        self.first_order_url = first_order_response.data['url']
        self.first_orders_first_ordered_pizza_url = first_order_response.data['ordered_pizzas'][0]['url']


    def test_order_pizza(self):
        """
        Ensure we can order pizza.
        """
        response = self.client.post(
            self.orders_endpoint, 
            {
                "customer_id": 4,
                "is_paid": False,
                "ordered_pizzas": [
                    {
                        "count": 4,
                        "size": "s",
                        "pizza_flavor": "Pepperoni"
                    },
                    {
                        "count": 1,
                        "size": "m",
                        "pizza_flavor": "Margarita"
                    }
                ]
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)

    def test_update_order(self):
        """
        Ensure we can update fields of an order
        """
        response = self.client.patch(
            self.first_order_url,
            {
                "is_paid": True
            },
            format='json'
        )
        self.assertEqual(response.data['is_paid'], True)
        response = self.client.patch(
            self.first_order_url,
            {
                "is_paid": False
            },
            format='json'
        )
        self.assertEqual(response.data['is_paid'], False)
        self.assertEqual(response.status_code, 200)

    def test_update_orderedPizza(self):
        """
        Ensure we can update the details — flavours, count, sizes — of an order
        """
        response = self.client.patch(
            self.first_orders_first_ordered_pizza_url,
            {
                "pizza_flavor": "Margarita",
                "count": 3,
                "size": "s"
            },
            format='json'
        )
        self.assertEqual(response.data['pizza_flavor'], "Margarita")
        self.assertEqual(response.data['count'], 3)
        self.assertEqual(response.data['size'], "s")
        response = self.client.patch(
            self.first_orders_first_ordered_pizza_url,
            {
                "pizza_flavor": "Neapolitan",
                "count": 1,
                "size": "l"
            },
            format='json'
        )
        self.assertEqual(response.data['pizza_flavor'], "Neapolitan")
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['size'], "l")
        self.assertEqual(response.status_code, 200)

    def test_get_orders(self):
        """
        Ensure we can get the orders at once
        """
        number_of_orders = Order.objects.all().count()
        response = self.client.get(self.orders_endpoint)
        self.assertEqual(len(response.data), number_of_orders)
        self.assertEqual(response.data[0]['url'], self.first_order_url)
        self.assertEqual(response.status_code, 200)

    def test_get_orders_filter_by_status_and_customer(self):
        """
        Ensure we can filter orders by status and customer
        """
        response = self.client.get(
            self.orders_endpoint, 
            {
                'delivery__status': 'not_ready',
                'customer_id': 2
            }
        )
        number_of_filtered_orders = Order.objects.filter(delivery_detail__status='not_ready', customer_id=2).count()
        self.assertEqual(len(response.data), number_of_filtered_orders)
        for order in response.data:
            self.assertEqual(order['delivery_detail']['status'], 'not_ready')
            self.assertEqual(order['customer_id'], 2)
        self.assertEqual(response.status_code, 200)

