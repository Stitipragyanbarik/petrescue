from django import forms
from .models import Pet


class ReportPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species','breed','gender',  'age','color', 'description', 'image','location','contact_phone', 'status', 'animal_condition', 'last_seen_location', 'medical_attention_needed']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
             'species': forms.TextInput(attrs={'placeholder': 'Dog, Cat, etc.'}),
            'gender': forms.Select(choices=[('Male','Male'),('Female','Female')]),
            'animal_condition': forms.Select(attrs={'class': 'form-control'}),
        }


class ContactMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':4}), max_length=2000)


class ImageCheckForm(forms.Form):
    image = forms.ImageField(required=True)
