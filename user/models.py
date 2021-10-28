from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class tbl_student(models.Model):
    CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    student_name       = models.CharField(max_length=30)
    college_name       = models.CharField(max_length=50)
    specialisation      = models.CharField(max_length=30)
    degree_name        = models.CharField(max_length=30)
    internship_applied = models.CharField(max_length=100)
    phone_no           = PhoneNumberField()
    email_id           = models.EmailField(max_length=50)
    location           = models.TextField()
    gender             = models.CharField(max_length=30, choices = CHOICES)
    notes              = models.TextField()

    def __str__(self) -> str:
        return self.student_name
