from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# Create your models here.



class UserWithPhone(AbstractUser):
    phone = models.CharField("Номер телефона", max_length=50)


User = get_user_model()

class Service(models.Model):
    name = models.CharField("Название услуги", max_length=50)
    price = models.DecimalField("Цена", max_digits=5, decimal_places=2)


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    comment = models.TextField()
    status = models.IntegerField('Статус заявки',choices=[
        (0,'Новая'),
        (1,'Принята'),
        (2,'Выполнена')
    ])
    created_at = models.DateField("Дата создания", auto_now=True)
    class Meta:
        verbose_name='Заявка'
        verbose_name_plural = 'Заявки'


