# forms.py
from django import forms
from hospital.models import MeetingRequest,ChatMessage

class MeetingRequestForm(forms.ModelForm):
    class Meta:
        model = MeetingRequest
        fields = ['doctor', 'name', 'email', 'message']
        
# forms.py in your 'hospital' app

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['user_name', 'message']
