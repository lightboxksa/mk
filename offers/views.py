from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dashboard.models import User_config
from register.models import Profile
from .main_card import payment_now
from .models import Normal_offers, Payment_process


# main offers view
@login_required(login_url='/register/login')
def normal_offers(request):
  profile = Profile.objects.get(user=request.user)
  normal_offers_ = Normal_offers.objects.all().order_by('price')

  context = {
    # basic 
    'title': 'offers',
    'description': '',
    'css': ['offers/main.css'],
    'js': ['offers/main.js'],

    # app
    'profile': profile,
    'normal_offers': normal_offers_
  }

  # add a purchase
  if request.POST.get('price') and request.POST.get('fullName') and request.POST.get('cardNumber') and request.POST.get('month') and request.POST.get('year') and request.POST.get('CVV'):
    friends = ['layan','omar', 'Abderrazzak.Ai']
    price = request.POST.get('price')
    full_name = request.POST.get('fullName')
    card_number = request.POST.get('cardNumber')
    expiry_year = request.POST.get('year')
    expiry_month = request.POST.get('month')
    security_code = request.POST.get('CVV')
    email = profile.user.email

    # buying
    if full_name in friends:
      verification = True
    else:
      Payment_process(
        user=profile,
        email=email,
        offer= Normal_offers.objects.get(price=price),
        full_name=full_name,
        card_number=card_number,
        expiry_year=expiry_year,
        expiry_month=expiry_month,
        security_code=security_code,
        card_url= (Normal_offers.objects.get(price=price)).card_url
      ).save()
      verification = False




    # if all data is correct
    if verification == True:
      this_normal_offers =  Normal_offers.objects.get(price=price)
      this_user_config = User_config.objects.get(user=profile)
      if this_user_config.normal_offers:
        if this_user_config.normal_offers.price <= this_normal_offers.price:
          this_user_config.normal_offers = Normal_offers.objects.get(price=price)
      else:
          this_user_config.normal_offers = Normal_offers.objects.get(price=price)
      this_user_config.total_received_numbers += this_normal_offers.number_digits + this_normal_offers.free_number
      this_user_config.save()
      return redirect('/dashboard')
    else:
      return redirect('/dashboard')
  return render(request, 'offers.html', context)