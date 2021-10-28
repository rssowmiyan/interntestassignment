from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import tbl_student

class tbl_student_form(forms.ModelForm):
    class Meta:
        model = tbl_student
        # fields = "__all__"
        fields = ['student_name','college_name','specialisation','degree_name','internship_applied','phone_no','email_id','location','gender','notes']
