from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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


class ServiceManInfo(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pic',blank=True)
    #type_appliance_service=models.CharField(max_length=50,choices=sorted(appliance_type_CHOICES))
    #pincode_service=models.PositiveIntegerField()

    def __str__(self):
        return  self.user.username