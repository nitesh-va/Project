from django.db import models
from django.utils import timezone

# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def count(self):
        return self.get_queryset().count()
    
    def is_active(self):
        return self.get_queryset().filter(is_active=True)
    
    def is_inactive(self):
        return self.get_queryset().filter(is_active=False)
        
class School(models.Model):
    name = models.CharField(max_length=100)  # School name
    school_id = models.IntegerField(primary_key=True)  # Primary key
    location = models.CharField(max_length=255)  # School location
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active = ActiveManager()

    def __str__(self):
        return self.name