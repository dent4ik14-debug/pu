from django.db import models
from django.contrib.auth.models import AbstractUser
from service.models import Service
# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        MASTER = 'master', 'мастер'
        USER = 'user', 'користувач'
    role = models.CharField(
        'роль',
        max_length=10,
        choices=Role.choices,
        default=Role.USER
    )

class MasterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    experience = models.PositiveIntegerField(default=0, verbose_name="Досвід роботи (місяці)")
    def __str__(self):
        return f"Ім'я майстра:{self.user.first_name} | Рейтинг: {self.rating}"

class MasterService(models.Model):
    master = models.ForeignKey(MasterProfile, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_minutes = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f'Майстер: {self.master.user.first_name} | Ціна: {self.price} | Тривалість: {self.duration_minutes}'