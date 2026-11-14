from django import forms
from .models import NutrientFeed


class NutrientFeedForm(forms.ModelForm):
    class Meta:
        model = NutrientFeed
        fields = ['bioreactor', 'completed_date', 'is_completed', 'notes']
        widgets = {
            'bioreactor': forms.Select(attrs={'class': 'form-control'}),
            'completed_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }