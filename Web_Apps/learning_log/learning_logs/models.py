from django.db import models

# Create your models here.

class Topic(models.Model):
    #Our first model is called Topics, inheriting from Model-class from models module.
    # It defines a models basic functionality.

    """A topic the user is learning about."""
    text = models.CharField(max_length=200) #Text attribute.
    #In Django, CharField is a piece of data made up by characters.
    # You use CharField when you want to store a small amount of text.
    #  CharField needs max_length attribute, defining maximum amount of characters it can hold.
    #   200 should be enough for a topic name.

    date_added = models.DateTimeField(auto_now_add=True) #Attribute to check when a new topic is created.
    #DateTimeField is a piece of data that will record a date and time for us.
    # The auto_now_add tells Django to...
    #  auto-set this attribute to the current date and time whenever the user creates a new topic, if True.

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
