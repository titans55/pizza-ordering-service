from django.db import models
from django.urls import reverse


class PizzaFlavor(models.Model):

    #  Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    s_size_price = models.PositiveSmallIntegerField(null=True)
    m_size_price = models.PositiveSmallIntegerField(null=True)
    l_size_price = models.PositiveSmallIntegerField(null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("api_PizzaFlavor_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("api_PizzaFlavor_update", args=(self.id,))


class OrderedPizza(models.Model):

    #  Fields
    id = models.AutoField(primary_key=True)
    size = models.CharField(
        max_length=1,
        choices=[
            ('s', 'Small'),
            ('m', 'Medium'),
            ('l', 'Large'),
        ]
    )
    count = models.PositiveSmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    #  Relationships
    pizza_flavor = models.ForeignKey("api.PizzaFlavor", on_delete=models.CASCADE)
    order = models.ForeignKey(
        'api.Order',
        on_delete=models.CASCADE,
        related_name="ordered_pizzas", 
    )
    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("api_OrderedPizza_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("api_OrderedPizza_update", args=(self.id,))


class Order(models.Model):

    #  Fields
    id = models.AutoField(primary_key=True)
    customer_id = models.PositiveIntegerField(default=1) #would be a foreign key when Customer model created
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    is_paid = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    #  Relationships
    delivery_detail = models.OneToOneField("api.DeliveryDetail", on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("api_Order_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("api_Order_update", args=(self.id,))


class DeliveryDetail(models.Model):

    #  Fields
    id = models.AutoField(primary_key=True)
    assigned_courier_id = models.PositiveIntegerField(default=1, null=True) #would be a foreign key when Courier model created
    status = models.CharField(
        max_length=30,
        choices=[
            ('not_ready', 'Not ready'),
            ('on_the_way', 'On the way'),
            ('delivered', 'Delivered'),
        ],
        default='not_ready'
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("api_DeliveryDetail_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("api_DeliveryDetail_update", args=(self.id,))