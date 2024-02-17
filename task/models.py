from django.db import models
from categories.models import Categories


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    category = models.ManyToManyField(Categories)
    due_date = models.DateField()

    def __str__(self):
        return self.title
