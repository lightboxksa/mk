from offers.models import Normal_offers, Offers
from register.models import Profile
from django.db import migrations
import random
from django.db import models


# getcurrentusername
def getcurrentusername(instance, filename):
  new_sh = ''.join(random.sample('abcdefghijklmnopkrstivwxyzABCDEFGHIJKLMNOPKRSTIVWXYZ1234567890', 20))
  return f"imgaes/users/{instance.user}/Tasks/{instance.name}/{new_sh}"


# tasks
class Tasks(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  message = models.TextField(max_length=1000)
  is_image = models.BooleanField(default=False, null=True, blank=True)
  image = models.ImageField(upload_to=getcurrentusername, null=True, blank=True)
  image_url = models.CharField(max_length=1000, default="")
  name = models.CharField(max_length=50)
  job = models.CharField(max_length=50, default="all")
  gender = models.CharField(choices=[('male', 'male'), ('female','female')], max_length=50, default="all")
  country = models.CharField(max_length=50,  default="all")
  city = models.CharField(max_length=50,  default="all")  
  range = models.IntegerField()
  available = models.BooleanField(default=True)
  added_date = models.DateTimeField(auto_now=True)
  received_numbers = models.TextField(max_length=100000, default="")

  def __str__(self):
    return self.name

# sent numbers
class Sent_Numbers(models.Model):
  phone_number = models.CharField(max_length=50)
  country = models.CharField(max_length=50, default="unknown")
  available = models.BooleanField(default=True)

  def __str__(self):
    return self.phone_number

# received numbers
class Received_Numbers(models.Model):
  phone_number = models.CharField(max_length=50)
  name = models.CharField(max_length=50)
  job = models.CharField(max_length=50, null=True, blank=True)
  gender = models.CharField(choices=[('male', 'male'), ('female','female')], max_length=50, default="unknown")
  country = models.CharField(max_length=50,  null=True, blank=True)
  city = models.CharField(max_length=50,  null=True, blank=True)

  def __str__(self):
    return self.phone_number

# message
class Message(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  task = models.ForeignKey(Tasks, related_name='+', on_delete=models.CASCADE)
  # received_number = models.CharField(max_length=50)
  status = models.CharField(choices=[('wait', 'wait'), ('sended','sended')], max_length=50, default='wait')
  date_send = models.IntegerField(default=0)
  added_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.task.name

# user config
class User_config(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  # normal_offers = models.ForeignKey(Normal_offers, on_delete=models.CASCADE, null=True, blank=True)
  offer = models.ForeignKey(Offers, on_delete=models.CASCADE, null=True, blank=True)
  total_received_numbers = models.IntegerField(default=0)
  numbers_of_one_ad = models.IntegerField(default=0)

  def __str__(self):
    return str(self.user)



# Country
class Country(models.Model):
  country = models.CharField(max_length=50)

  def __str__(self):
    return self.country

# City
class City(models.Model):
  country = models.ForeignKey(Country, on_delete=models.CASCADE)
  city = models.CharField(max_length=50,)

  def __str__(self):
    return self.city

# Job
class Job(models.Model):
  job = models.CharField(max_length=50)

  def __str__(self):
    return self.job





# page controler
class Page_Controler(models.Model):
  title = models.CharField(max_length=50)
  hover_title = models.CharField(max_length=100)
  url = models.URLField(max_length=100)
  new_tab = models.BooleanField(default=False)
  activate = models.BooleanField(default=True)

  def __str__(self):
    return self.title