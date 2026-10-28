from django.db import models

# Create your models here.
class ServiceCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Service(models.Model):
    name =  models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    #master
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Назва:{self.name} | Категорія:{self.category}'