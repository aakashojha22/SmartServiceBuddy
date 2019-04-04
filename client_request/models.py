from django.db import models
from django.utils import timezone
from django.shortcuts import redirect
from service_man.models import  ServiceManInfo

# Create your models here.
appliance_brand_CHOICES = (
    ('lg','LG'),
    ('samsung', 'Samsung'),
    ('sony','Sony'),
    ('bajaj','Bajaj'),
    ('godrej','Godrej'),
    ('carrier','Carrier'),
    ('philips','Philips'),
    ('toshiba','Toshiba'),
    ('panasonic','Panasonic'),
    ('onida','Onida'),
    ('sharp','Sharp'),
    ('mi','MI'),
    ('whirlpool','Whirlpool'),
    ('haier','Haier'),
    ('ifb','IFB'),
    ('voltas','Voltas'),
    ('hitachi','Hitachi'),
    ('blue star','Blue Star'),
    ('other', 'Other'),

)
appliance_type_CHOICES = (
    ('refrigerator','Refrigerator'),
    ('microwave oven', 'Microwave oven'),
    ('washing machine', 'Washing machine'),
    ('dishwasher', 'Dishwasher'),
    ('air conditioner', 'Air conditioner'),
    ('water heater', 'Water heater'),
    ('air purifier', 'Air purifier'),
    ('ceiling fan', 'Ceiling fan'),
    ('vacuum Cleaner', 'Vacuum Cleaner'),
    ('hair dryer', 'Hair dryer'),
    ('water purifier', 'Water purifier'),
    ('other', 'Other'),
)
warranty_CHOICES = (
    ('pre warranty', 'Pre Warranty'),
    ('post warranty','Post Warranty'),
     )
class ClientRequest(models.Model):
    
    #detail_by_client
    name = models.CharField(max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    pincode = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    appliance_type  = models.CharField(max_length=50,choices=sorted(appliance_type_CHOICES))
    appliance_brand = models.CharField(max_length=50,choices=sorted(appliance_brand_CHOICES))
    appliance_model = models.CharField(max_length=50)
    warranty = models.CharField(max_length=50,choices=(warranty_CHOICES))
    problem_description = models.CharField(max_length=200)
    request_date = models.DateTimeField(default=timezone.now)
    appointment_date= models.DateField()
    appointment_time = models.TimeField(blank=True,null=True)
    
    #for_admin
    verfication_status = models.BooleanField(default=False)
    service_man = models.ForeignKey(ServiceManInfo, related_name='serivce_man_appointed', on_delete=models.CASCADE,null=True,blank=True)

    email_verification =  models.BooleanField(default=False)
    charge = models.PositiveIntegerField(blank=True,null=True)
    
    
    
    def get_absolute_url(self):
        return redirect("thankyou")
    
    def __str__(self):
        return self.email

