from django.db import models

# Create your models here.

class Topic(models.Model):
    #Our first model is called Topic, inheriting from Model-class from models module.
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
        #We tell Django which attribute to use by default when it displays info about a topic using __str__ method.
        # Django calls a __str__ method to display a simple representation of a model.
        """Return a string representation of the model."""
        return self.text
        #This __str__() returns the string stored in the text attribute.


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    #We assign the topic attribute a ForeignKey instance.
    # A "foreign key" is a database term, a reference to another record in the database.
    #  The foreign key is what connects each entry to a specific topic.
    #   Whenever a Topic is created, it's associated with a key or an ID.
    #    When Django connects two pieces of data, it uses the keys associated with each piece of info.
    #The second argument 'on_delete=models.CASCADE' tells Django that...
    # when a Topic is deleted, it should also delete all the entries associated with that topic.
    #  This kind of delete is generally called a "cascading delete".

    text = models.TextField()
    #The text attribute is an instance of TextField, which is a field without any limits.

    date_added = models.DateTimeField(auto_now_add=True)
    #Like in the Topics model, we use the DateTimeField to record when an entry is created.
    # We'll use this to sort entries and display creation date.

    class Meta:
        verbose_name_plural = 'entries'
        #Here we nest a Meta-class inside our model-class.
        # The Meta class holds extra information for managing a model.
        #  verbose_name_plural allows us to set a special name when the model is referred to in plural.
        #   This tells Django to use Entries instead of Entrys as it would do by default.

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text
        #The __str__ method tells Django which information to show when it refers to individual entries,
        # If the str is long, we also add the three dots at the end (called ellipsis) to clarify it's long.
