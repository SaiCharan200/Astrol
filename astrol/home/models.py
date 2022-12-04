from django.db import models
import crispy_forms


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=122)
    city = models.CharField(max_length=50, default="null")
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.CharField(max_length=122, default="null")

    def __str__(self):
        return self.name


class Login(models.Model):
    username = models.CharField(max_length=30, default="null")
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username


class User(models.Model):
    firstname = models.CharField(max_length=15)
    middlename = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.firstname + self.middlename + self.lastname


class Report(models.Model):
    firstname = models.CharField(max_length=20,default="")
    lastname = models.CharField(max_length=20,default="")
    gender = models.CharField(max_length=1,default="")
    date = models.IntegerField(default="")
    month = models.IntegerField(default="")
    year = models.IntegerField(default="")

    def __str__(self):
        return self.firstname


class Traits(models.Model):
    Nakshatra=models.CharField(max_length=20,default="")
    positive=models.TextField(max_length=None,default="")
    negative = models.TextField(max_length=None, default="")


class Rashi(models.Model):
    Nakshatra=models.CharField(max_length=20,default="")
    rashi=models.CharField(max_length=20,default="")