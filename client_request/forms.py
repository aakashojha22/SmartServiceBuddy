from django import forms
from client_request.models import ClientRequest
from django.contrib.admin.widgets import AdminDateWidget
class ClientRequestForm(forms.ModelForm):
    class Meta:
        model = ClientRequest
        fields=('name','mobile','email','pincode','address','appliance_type','appliance_brand','appliance_model','warranty','problem_description','appointment_date')

