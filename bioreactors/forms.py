from django import forms
from .models import AlgaeSpecies, BioreactorUnit, Equipment


class AlgaeSpeciesForm(forms.ModelForm):

    class Meta:
        model = AlgaeSpecies
        fields = '__all__'
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'feed_interval_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'optimal_temp': forms.NumberInput(attrs={'class': 'form-control'}),
            'target_ph': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_target_ph(self):
        ph = self.cleaned_data.get('target_ph')
        if ph < 0 or ph > 14:
            raise forms.ValidationError(
                'Target pH must be a realistic value between 0 and 14.'
            )
        return ph


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'e.g., pH Sensor'}
            )
        }


class BioreactorUnitForm(forms.ModelForm):

    class Meta:
        model = BioreactorUnit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Unit Alpha'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Shelf 1'}),
            'algae_species': forms.Select(attrs={'class': 'form-control'}),
            'equipment': forms.CheckboxSelectMultiple(),
            'setup_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'progress_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'observations': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class BioreactorUpdateForm(forms.ModelForm):

    class Meta:
        model = BioreactorUnit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'algae_species': forms.Select(attrs={'class': 'form-control'}),
            'equipment': forms.CheckboxSelectMultiple(),
            'setup_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'progress_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'observations': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['setup_date'].disabled = True
        self.fields['setup_date'].help_text = 'Setup date cannot be changed after creation.'