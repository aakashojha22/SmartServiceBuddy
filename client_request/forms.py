from django import forms
from client_request.models import ClientRequest
from django.forms import SelectDateWidget
from datetime import date

class ClientRequestForm(forms.ModelForm):
    appointment_date = forms.DateField(widget = SelectDateWidget)
    class Meta:
        model = ClientRequest
        fields=('name','mobile','email','pincode','address','appliance_type','appliance_brand','appliance_model','warranty','problem_description','appointment_date')

    def clean(self):

        # data from the form is fetched using super function
        super(ClientRequestForm, self).clean()

        # extract the username and text field from the data
        mobile = str(self.cleaned_data.get('mobile'))
        pincode = str(self.cleaned_data.get('pincode'))
        name=self.cleaned_data.get('name')
        appointment_date=self.cleaned_data.get('appointment_date')

        # conditions to be met for the username length
        if len(mobile) != 10:
            self._errors['mobile'] = self.error_class([
                'Minimum 10 characters required'])
        if len(pincode) != 6:
            self._errors['pincode'] = self.error_class([
                'Pincode Should Contain minimum 6 characters'])
        if appointment_date < date.today():
            self._errors['appointment_date'] = self.error_class([
                'Please select future date'])

        return self.cleaned_data


class UpdateClientRequestForm(forms.ModelForm):
    class Meta:
        model = ClientRequest
        fields=('charge','request_status')
"""
    def clean(self):

        # data from the form is fetched using super function
        super(ClientRequestForm, self).clean()

        # extract the username and text field from the data
        mobile = str(self.cleaned_data.get('mobile'))
        pincode = str(self.cleaned_data.get('pincode'))
        name=self.cleaned_data.get('name')
        appointment_date=self.cleaned_data.get('appointment_date')

        # conditions to be met for the username length
        if len(mobile) != 10:
            self._errors['mobile'] = self.error_class([
                'Minimum 10 characters required'])
        if len(pincode) != 6:
            self._errors['pincode'] = self.error_class([
                'Pincode Should Contain minimum 6 characters'])
        if appointment_date < date.today():
            self._errors['appointment_date'] = self.error_class([
                'Please select future date'])

        return self.cleaned_data
"""