from django.db import models
from register.models import Profile

# normal offers
class Normal_offers(models.Model):
  price = models.DecimalField(max_digits=10,  decimal_places=2)
  number_digits = models.IntegerField()
  free_number = models.IntegerField(default=0)
  numbers_of_one_ad = models.IntegerField(default=100)
  numbers_of_one_ad_text = models.CharField(max_length=28, default="لم يتم تخصيص نص")
  text_1 = models.CharField(max_length=28, default="لم يتم تخصيص نص")
  text_2 = models.CharField(max_length=28, default="لم يتم تخصيص نص")
  message_type = models.CharField(choices=[('text', 'text'), ('text + image', 'text + image')], max_length=50, default='text')
  message_type_text = models.CharField(max_length=28, default="لم يتم تخصيص نص")
  # unique_id = models.CharField(max_length=28, null=True, blank=True)
  card_url = models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
    return f'${self.price}'

class Offers(models.Model):
  price = models.DecimalField(max_digits=10,  decimal_places=2)
  number_digits = models.IntegerField()
  numbers_of_one_ad = models.IntegerField(default=100)
  message_type = models.CharField(choices=[('text', 'text'), ('text + image', 'text + image')], max_length=50, default='text')
  product_id = models.CharField(max_length=100)

  def __str__(self):
    return f'${self.price}'

class Payment_process(models.Model):
  payment_id = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  product_id = models.CharField(max_length=50)
  done = models.BooleanField(default=False)







# class Payment_process(models.Model):
#   user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#   email = models.CharField(max_length=50)
#   offer = models.ForeignKey(Normal_offers, on_delete=models.CASCADE)
#   full_name = models.CharField(max_length=50)
#   card_number = models.CharField(max_length=50)
#   expiry_year = models.CharField(max_length=50)
#   expiry_month = models.CharField(max_length=50)
#   security_code = models.CharField(max_length=50)
#   done = models.BooleanField(default=False)
#   available = models.BooleanField(default=True)
#   card_url = models.CharField(max_length=100, null=True, blank=True)
#   selenium_key = models.CharField(max_length=100, default="")
