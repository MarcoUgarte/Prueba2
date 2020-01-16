from django.db import models
from django.urls import reverse

# Create your models here.

class Client(models.Model):
    rut_client = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
