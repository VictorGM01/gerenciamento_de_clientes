from django.db import models
from django.urls import reverse


class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    birth_date = models.DateField()
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)  # Django armazena automaticamente a data de criação
    updated_date = models.DateTimeField(auto_now=True)  # Armazena data caso haja alteração
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('customer:customer-update', kwargs={'id': self.id})

    def get_delet_url(self):
        return reverse('customer:customer-delete', kwargs={'id': self.id})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'customer'  # Nomeia tabela
