# Register your models here.
from django.contrib import admin
from hospital.models import  ChatMessage, Department, Doctor, MeetingRequest


# Register your models here
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(MeetingRequest)
admin.site.register(ChatMessage)
