from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError
from school.models import ActiveManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        # Here we implement the natural key query method
        return self.get(username=username)



class User(AbstractBaseUser):
    username= models.CharField(max_length=100, default='', unique=True)
    email = models.EmailField(max_length=100,default='',unique=True)
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField(primary_key=True)
    performance = models.FloatField(default=0.0)
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    dept_name=models.ForeignKey('department.Department', on_delete=models.SET_NULL, null=True, blank=True)
    school_name=models.ForeignKey('school.School', on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(max_length=100, default='User')
    is_active=models.BooleanField(default=True)
    temp_pass = models.CharField(max_length=100, default='', blank=True, null=True)


    objects = CustomUserManager()
    active = ActiveManager()

    
    def save(self, *args, **kwargs):
        # Automatically generate and hash the password if it's not set
        if not self.password:
            random_password = get_random_string(length=8)  # Generate a random password
            self.temp_pass = random_password  # Store the random password temporarily
            self.password = make_password(random_password)  # Hash the password
        super().save(*args, **kwargs)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def validate_password(self, password):
        """Ensure the password meets required criteria without using regular expressions."""
        if len(password) < 8:
            raise ValidationError('Password must be at least 8 characters long.')
        
        has_upper = any(char.isupper() for char in password)  # Check for uppercase letter
        has_lower = any(char.islower() for char in password)  # Check for lowercase letter
        has_digit = any(char.isdigit() for char in password)  # Check for a digit
        has_special = any(char in '!@#$%^&*(),.?":{}|<>' for char in password)  # Check for special characters
        
        if not has_upper:
            raise ValidationError('Password must contain at least one uppercase letter.')
        if not has_lower:
            raise ValidationError('Password must contain at least one lowercase letter.')
        if not has_digit:
            raise ValidationError('Password must contain at least one number.')
        if not has_special:
            raise ValidationError('Password must contain at least one special character.')

    