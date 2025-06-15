from django.contrib import admin
from .models import Patient,Token,Department,Doctor
# Register your models here.
admin.site.register(Patient)
admin.site.register(Token)
admin.site.register(Department)
admin.site.register(Doctor)