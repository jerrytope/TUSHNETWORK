from django import forms
from .models import Release, Track

class ReleaseForm(forms.ModelForm):
    class Meta:
        model = Release
        fields = ['title', 'artist_name', 'release_type', 'genre', 'release_date', 'cover_art']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter release title'}),
            'artist_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter artist name'}),
            'release_type': forms.Select(attrs={'class': 'form-select'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Afrobeats, Hip Hop, R&B'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cover_art': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.required:
                field.widget.attrs['required'] = True

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'audio_file', 'duration', 'track_number']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter track title'}),
            'audio_file': forms.FileInput(attrs={'class': 'form-control', 'accept': 'audio/*'}),
            'duration': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'MM:SS'}),
            'track_number': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        }

# Formset for handling multiple tracks
TrackFormSet = forms.modelformset_factory(
    Track, 
    form=TrackForm, 
    extra=1, 
    can_delete=True,
    fields=['title', 'audio_file', 'duration', 'track_number']
)
