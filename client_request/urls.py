
from django.urls import path
from client_request import views
from django.conf.urls import url
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('our_services', views.OurServicesView.as_view(), name='our_service',),
    path('who_we_are', views.WhoWeAreView.as_view(), name='who_we_are'),
    path('faqs', views.FaqsView.as_view(), name='faqs'),
    path('career', views.CareerView.as_view(), name='career'),
    path('service_request', views.ServicesRequestView, name='service_request'),
    path('thankyou', views.ThankyouView.as_view(), name='thankyou'),
    path('search', views.SearchView.as_view(), name='search'),
    path('request_detail/<int:pk>/',views.RequestDetailView.as_view(),name='request_detail'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.email_verify, name='email_verify'),
]

