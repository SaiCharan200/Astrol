from django import forms
from .models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['firstname', 'lastname', 'gender', 'date', 'month', 'year']  # __all__
