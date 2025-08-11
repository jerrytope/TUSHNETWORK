from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, ArtistProfile, LabelProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    account_type = forms.ChoiceField(
        choices=CustomUser.ACCOUNT_TYPE_CHOICES,
        widget=forms.RadioSelect,
        initial='artist'
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'account_type')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        
        self.fields['account_type'].widget.attrs['class'] = 'form-check-input'

class ArtistProfileForm(forms.ModelForm):
    class Meta:
        model = ArtistProfile
        fields = ('stage_name', 'genre')
        widgets = {
            'stage_name': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LabelProfileForm(forms.ModelForm):
    class Meta:
        model = LabelProfile
        fields = ('label_name', 'founded_year', 'website')
        widgets = {
            'label_name': forms.TextInput(attrs={'class': 'form-control'}),
            'founded_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }