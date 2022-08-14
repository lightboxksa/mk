from django.contrib import admin
from .models import Tasks, Sent_Numbers, Received_Numbers, Message, User_config, Country, City, Job, Page_Controler

# Register your models here.

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Job)

admin.site.register(Received_Numbers)
admin.site.register(Sent_Numbers)


admin.site.register(User_config)
# admin.site.register(Tasks)
# admin.site.register(Message)
admin.site.register(Page_Controler)