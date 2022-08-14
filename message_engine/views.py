import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
import time

from register.models import Profile
from dashboard.models import Tasks, Sent_Numbers, Received_Numbers, Message
from dashboard.models import User_config

# Create your views here.
@login_required(login_url='/register/login')
def message_engine(request, id):
  today = datetime.datetime.today()

  task = Tasks.objects.get(id=id)
  if task.is_image:
    task.image_url = task.image.url
    task.save()
  profile = Profile.objects.get(user=request.user)
  user_config = User_config.objects.get(user=profile)
  user_config.total_received_numbers -= user_config.offer.numbers_of_one_ad

  user_config.save()





  if len(task.received_numbers) <= 5:
    job = task.job
    gender = task.gender
    country = task.country
    city = task.city
    if job == gender and country == gender:
      received_numbers = Received_Numbers.objects.all()
    
    elif job == gender and country != job:
      if city == job:
        received_numbers = Received_Numbers.objects.filter(country=country)
      else:
        received_numbers = Received_Numbers.objects.filter(country=country, city=city)

    elif job == 'all' and gender != job and country != job:
      received_numbers = Received_Numbers.objects.filter(country=country, city=city, gender=gender)
    
    elif gender != 'all' and job != 'all' and country != 'all':
      received_numbers = Received_Numbers.objects.filter(country=country, city=city, gender=gender, job=job)

    else:
      received_numbers = Received_Numbers.objects.all()

    filter_received_numbers = []
    if len(received_numbers) > user_config.offer.numbers_of_one_ad:
      received_numbers=received_numbers[:user_config.offer.numbers_of_one_ad]
    else:
      other = Received_Numbers.objects.all()[:user_config.offer.numbers_of_one_ad-len(received_numbers)]
      for number in other:
        filter_received_numbers.append(number.phone_number)

    for received_number in received_numbers:
      if received_number.phone_number not in filter_received_numbers:
        filter_received_numbers.append(received_number.phone_number)

    task.received_numbers = str(filter_received_numbers)
    task.save()

  # add new message to db

  data = (task.received_numbers[1:-1]).split(',')
  received_numbers = []
  for received_number in data:
    received_numbers.append(received_number[1:-1])
    
  Message(
    user=profile,
    task=task,
    status="wait",
    date_send= today.day).save()


  context = {
    # basic 
    'title': 'Message Engine',
    'description': '',
    'css': ['dashboard/main.css', 'message_engine/main.css'],
    'js': ['message_engine/main.js'],

    'profile': profile,
    'this_task': task,
    'numbers': received_numbers,
  }


  return render(request, 'message_engine.html', context)