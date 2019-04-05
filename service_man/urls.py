
from django.urls import path
from django.contrib.auth import views

from service_man import views as v

app_name='service_man'

urlpatterns = [

    path('',v.IndexView.as_view(),name='index'),
    path('pending_request',v.PendingRequestView.as_view(),name='pending_request'),
    path('past_request',v.PastRequestView.as_view(),name='past_request'),
    path('request_detail/<int:pk>/',v.RequestDetailView.as_view(),name='request_detail'),


    path('login',views.LoginView.as_view(template_name='service_man/login.html'),name='login'),
    path('logout',views.LogoutView.as_view(),name='logout'),

]



