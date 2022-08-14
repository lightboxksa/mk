import random
from .models import Tasks, Received_Numbers, Message, User_config, Country, City, Job, Page_Controler
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from register.models import Profile
from offers.models import Payment_process, Normal_offers, Offers
import datetime


# main dashboard view function
@login_required(login_url='/register/login')
def dashboard(request):
  today = datetime.datetime.today()
  profile = Profile.objects.get(user=request.user)


  # if payment
  if Payment_process.objects.filter(email=profile.user.email,done=False).exists():
    this_payments_process = Payment_process.objects.filter(email=profile.user.email,done=False)
    for payment_process in this_payments_process:
      if Offers.objects.filter(product_id=payment_process.product_id).exists():
        this_offer = Offers.objects.get(product_id=payment_process.product_id)
        this_user_config = User_config.objects.get(user=profile)
        if this_user_config.offer:
          if this_user_config.offer.price <= this_offer.price:
            this_user_config.offer = Offers.objects.get(product_id=payment_process.product_id)
        else:
            this_user_config.offer = Offers.objects.get(product_id=payment_process.product_id)
        this_user_config.total_received_numbers += this_offer.number_digits
        this_user_config.save()

        payment_process.done = True
        payment_process.save()



  # getsumple user info
  user_config = User_config.objects.get(user=profile)
  tasks = Tasks.objects.filter(user=profile).order_by('-added_date')

  if not user_config.offer:
    pass
  else:
    if user_config.total_received_numbers < user_config.offer.numbers_of_one_ad:
      for task in tasks:
        task.available = False
        task.save()
    else:
      for task in tasks:
        task.available = True
        task.save()
  

  available_tasks_len = len(Tasks.objects.filter(user=profile, available=True))
  tasks_len = len(tasks)


  # set context
  context = {
    # basic 
    'title': 'Dashboard',
    'description': '',
    'css': ['dashboard/main.css'],
    'js': ['dashboard/main.js'],
    'pages': Page_Controler.objects.all(),
    
    # app
    'profile': profile,
    'user_config': user_config,
    'tasks': tasks,
    'tasks_len': tasks_len,
    'available_tasks_len': available_tasks_len,
    'total_messages': len(Message.objects.filter(user=profile)),
    'todat_messages': len(Message.objects.filter(user=profile, date_send=today.day)),

    'countres': Country.objects.all(),
    'cites': City.objects.all(),
    'jobs': Job.objects.all(),
    
  }




  # add new tsak to db
  if request.POST.get('task_name') and request.POST.get('message'):
    if request.FILES.get("img_file"):
      image = request.FILES.get("img_file")
      is_image = True
    else:
      is_image = False
      image = None


    message = request.POST.get('message')
    task_name = request.POST.get('task_name')
    job = request.POST.get('job')
    gender = request.POST.get('gender')
    country = request.POST.get('country')
    city = request.POST.get('city')
    range = user_config.offer.numbers_of_one_ad

    Tasks(user=profile, 
          message=message,
          is_image=is_image,
          image = image,
          name=task_name,
          job=job,
          gender=gender,
          country=country, 
          city=city,
          range=range).save()
    return redirect('/dashboard')

  # if tsak tsart work
  if request.POST.get('start'):
    statu = str(request.POST.get('start')).split(',')[0]
    task_id = str(request.POST.get('start')).split(',')[1]
    task = Tasks.objects.get(id=int(task_id), user=profile)
    

    # delete task
    if statu == 'delet' and task_id:
      task.delete()
      return redirect('/dashboard')

    # start task work
    # elif statu == 'start' and task_id:
    #   pass

  # user logout
  if request.POST.get('logout') == 'True':
    logout(request)
    return redirect('/register/login')
  return render(request, 'dashboard.html', context)