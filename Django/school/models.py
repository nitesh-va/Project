from django.db import models
from django.utils import timezone
# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)  # School name
    school_id = models.IntegerField(primary_key=True)  # Primary key
    location = models.CharField(max_length=255)  # School location
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name