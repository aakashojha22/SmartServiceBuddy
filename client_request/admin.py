from django.contrib import admin
from client_request.models  import ClientRequest
# Register your models here.

class ClientRequestAdmin(admin.ModelAdmin):
    search_fields = ['mobile','email','name']

    list_filter = ['verfication_status','service_man','email_verification','request_status']

    list_display = ['email','name','appointment_date','request_date','verfication_status','service_man',
                    'email_verification','request_status']




admin.site.register(ClientRequest,ClientRequestAdmin)