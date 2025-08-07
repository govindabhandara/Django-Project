from django.contrib import admin
from .models import contactEnquiry

class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')  # Fields to display in the table

# Register the model with the custom admin
admin.site.register(contactEnquiry, ContactEnquiryAdmin)
