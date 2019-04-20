from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,UpdateView,DeleteView )
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from service_man.models import ServiceManInfo
from client_request.models import ClientRequest
from client_request.forms import ClientRequestForm, UpdateClientRequestForm



# Create your views here.

class IndexView(TemplateView):
    template_name = 'service_man/index.html'


class PendingRequestView(ListView,LoginRequiredMixin):
    model = ClientRequest
    template_name = 'service_man/pending_request.html'
    def get_queryset(self):
       return ClientRequest.objects.filter(appointment_date__gte=timezone.now(),request_status='service_pending').order_by('appointment_date')

class PastRequestView(ListView,LoginRequiredMixin):
    model = ClientRequest
    template_name = 'service_man/past_request.html'
    def get_queryset(self):
       return ClientRequest.objects.filter(appointment_date__lt=timezone.now() ,request_status='service_done').order_by('-appointment_date')

class ServiceDoneRequestView(ListView,LoginRequiredMixin):
    model = ClientRequest
    template_name = 'service_man/service_done_request.html'
    def get_queryset(self):
       return ClientRequest.objects.filter(request_status='service_done').order_by('-appointment_date')




class RequestDetailView(DetailView,LoginRequiredMixin):
    model = ClientRequest
    template_name = 'service_man/request_detail.html'
"""
def ServicesRequestUpdateView(request,pk):
    form = UpdateClientRequestForm()
    user = ClientRequest.objects.get(pk=pk)
    if request.method == "POST":
        form = UpdateClientRequestForm(request.POST)
        if form.is_valid():

            request_detail = form.save(commit=True)
            #charge = form.cleaned_data['charge']
            #user.charge = charge
            request_detail.save()
    return render(request,'service_man/update_request_form.html')
"""
class ServicesRequestUpdateView(UpdateView,LoginRequiredMixin,):
    model = ClientRequest
    template_name = 'service_man/update_request_form.html'
    form_class = UpdateClientRequestForm
    login_url = 'service_man/login'
    #redirect_field_name = 'request_detail'
    success_url = reverse_lazy('service_man:pending_request')

