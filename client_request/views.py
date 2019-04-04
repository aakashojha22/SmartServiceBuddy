from django.views.generic import (TemplateView,CreateView,ListView,DetailView )
from client_request.models import ClientRequest
from .forms import ClientRequestForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import email_verification
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

class WhoWeAreView(TemplateView):
    template_name = 'who_we_are.html'

class OurServicesView(TemplateView):
    template_name = 'our_services.html'

class FaqsView(TemplateView):
    template_name = 'faqs.html'

class CareerView(TemplateView):
    template_name = 'be_a_part_of_us.html'
"""
class ServicesRequestView(View):
    #template_name = 'service_request_form.html'
    form_class = ClientRequestForm
    #success_url = 'thankyou'
    model = ClientRequest
"""
def ServicesRequestView(request):
        form = ClientRequestForm()
        if request.method == "POST":
            form = ClientRequestForm(request.POST)
            if form.is_valid():
                request_detail = form.save(commit=True)
                request_detail.save()
                current_site = get_current_site(request)
                mail_subject='Please Verify Your Email-SmartServiceBuddy'
                to_email = form.cleaned_data['email']
                #args = (request_detail.pk,)
                message = render_to_string('email_verification.html', {
                    'request_detail': request_detail,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(request_detail.pk)).decode(),
                    'token': email_verification.make_token(request_detail),
                })
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                
                
                return redirect('thankyou') 
        return render(request,'service_request_form.html',{'form':form})


def email_verify(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = ClientRequest.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and email_verification.check_token(user, token):
        user.email_verification = True
        user.save()
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

class ThankyouView(TemplateView):
    template_name = 'thankyou.html'



class SearchView(ListView):
    template_name = 'search_list.html'
    model = ClientRequest
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(Q(mobile__icontains=query)|Q(email__icontains=query))


        else:
            object_list = self.model.objects.none()
        return object_list


"""
class ProfileList(ListView):
    template_name = 'your_template.html'
    model = Profile

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(name__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list

def search_request(request):
    template='search_list.html'
    query=request.GET.get('q')
    if query:
        result = ClientRequest.objects.filter(email__icontains=query)
    else:
        result=ClientRequest.objects.all()
    return render(result,template,{'result': result})
"""

class RequestDetailView(DetailView):
    model = ClientRequest
    template_name = 'request_detail.html'


