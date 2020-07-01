from django.db import models

class Pizza(models.Model):
    """A Pizza model."""
    name = models.CharField(max_length=100)

    def __str__(self):
        """Return a string-representation of the model."""
        return self.name


class Topping(models.Model):
    """Specific toppings customers can choose."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        """Return a string-representation of the topping."""
        return self.name