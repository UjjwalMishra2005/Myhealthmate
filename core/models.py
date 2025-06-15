from django.db import models
from django.contrib.auth.models import AbstractUser

class Patient(AbstractUser):
    full_name = models.CharField(max_length=50, null=True, blank=True)
    adhaar_number = models.CharField(max_length=12, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=40, null=True, blank=True)
    # date_of_birth = models.DateTimeField(null=False, blank=False)
    gender = models.CharField(max_length=10, null=True, blank=True)
from django.db import models
from django.utils import timezone
class Token(models.Model):
    patient = models.ForeignKey('core.Patient', on_delete=models.CASCADE, unique=True)
    token_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    served_at = models.DateTimeField(null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    center_name = models.CharField(max_length=100, null=True, blank=True)
    center_code = models.CharField(max_length=20, null=True, blank=True)
    class Meta:
        unique_together = ( 'center_code', 'token_number')

    def save(self, *args, **kwargs):
        if not self.pk:  # Only assign token_number on creation
            today = timezone.now().date()
            last_token = Token.objects.filter(
                created_at__date=today,
                center_code=self.center_code
            ).order_by('-token_number').first()
            self.token_number = (last_token.token_number + 1) if last_token else 1
        super().save(*args, **kwargs)
class Department (models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Departments"
class Doctor(models.Model):
    name =  models.CharField(max_length=40,null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


    def __str__(self):
        return f" {self.name}"