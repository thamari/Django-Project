from django import forms
from .models import EmployeeDetails

class EmpForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = "__all__"
