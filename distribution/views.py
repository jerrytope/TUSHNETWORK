from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import modelformset_factory
from .models import Release, Track
from .forms import ReleaseForm, TrackForm, TrackFormSet

@login_required
def upload_release(request):
    if request.method == 'POST':
        release_form = ReleaseForm(request.POST, request.FILES)
        track_formset = TrackFormSet(request.POST, request.FILES, queryset=Track.objects.none())
        
        if release_form.is_valid() and track_formset.is_valid():
            # Save release
            release = release_form.save(commit=False)
            release.user = request.user
            release.save()
            
            # Save tracks
            for track_form in track_formset:
                if track_form.cleaned_data and not track_form.cleaned_data.get('DELETE', False):
                    track = track_form.save(commit=False)
                    track.release = release
                    track.save()
            
            messages.success(request, 'Release uploaded successfully! It will be reviewed within 24-48 hours.')
            return redirect('release_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        release_form = ReleaseForm()
        track_formset = TrackFormSet(queryset=Track.objects.none())
    
    context = {
        'release_form': release_form,
        'track_formset': track_formset,
    }
    return render(request, 'distribution/upload.html', context)

@login_required
def release_list(request):
    releases = request.user.releases.all().order_by('-created_at')
    return render(request, 'distribution/list.html', {'releases': releases})