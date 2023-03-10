from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


# Create your models here.
class UserManage(AbstractUser):
    username = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.username





class DGU(models.Model):
    mualliflarnomi = models.TextField(max_length=500, null=True, blank=True)
    fakultetnomi = models.TextField(max_length=500, null=True, blank=True)
    kafedranomi = models.TextField(max_length=500, null=True, blank=True)
    nomi = models.TextField(max_length=500, null=True, blank=True)
    Raqami = models.TextField(max_length=200, null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nomi


class BGU(models.Model):
    mualliflarnomi = models.TextField(max_length=500, null=True, blank=True)
    fakultetnomi = models.TextField(max_length=500, null=True, blank=True)
    kafedranomi = models.TextField(max_length=500, null=True, blank=True)
    nomi = models.TextField(max_length=500, null=True, blank=True)
    Raqami = models.TextField(max_length=200, null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nomi


class Patent(models.Model):
    mualliflarnomi = models.TextField(max_length=500, null=True, blank=True)
    fakultetnomi = models.TextField(max_length=500, null=True, blank=True)
    kafedranomi = models.TextField(max_length=500, null=True, blank=True)
    nomi = models.TextField(max_length=500, null=True, blank=True)
    Raqami = models.TextField(max_length=200, null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nomi


class MualliflikHuquqi(models.Model):
    mualliflarnomi = models.TextField(max_length=500, null=True, blank=True)
    fakultetnomi = models.TextField(max_length=500, null=True, blank=True)
    kafedranomi = models.TextField(max_length=500, null=True, blank=True)
    nomi = models.TextField(max_length=500, null=True, blank=True)
    Raqami = models.TextField(max_length=200, null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nomi


class News(models.Model):
    newsname = models.TextField(max_length=500, null=True, blank=True)
    text = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.newsname
