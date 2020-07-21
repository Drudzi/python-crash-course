from django.db import models

# Create your models here.
class BlogPost(models.Model):
    """A class modeling a blogpost."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the BlogPost object."""
        return self.title