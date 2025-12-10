from django import forms
from .models import Pet


class ReportPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'age', 'description', 'image', 'contact_phone', 'status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class ContactMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':4}), max_length=2000)


class ImageCheckForm(forms.Form):
    image = forms.ImageField(required=True)
