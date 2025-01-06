from django.db import models

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Optional field
    head = models.CharField(max_length=100)
    contact_info = models.TextField(blank=True, null=True)  # Optional field

    def __str__(self):
        return self.name

# Doctor Model
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors')
    availability = models.TextField(blank=True, null=True)  # Availability schedule, make optional

    def __str__(self):
        return self.name

# MeetingRequest Model (For scheduling meetings)
class MeetingRequest(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500)  # Limiting message length for better control
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Meeting with Dr. {self.doctor.name}"

#contact
class ChatMessage(models.Model):
    user_name = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.user_name}: {self.message[:50]}..."