from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ArtistProfileForm, LabelProfileForm
from .models import CustomUser

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('profile_setup')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile_setup(request):
    user = request.user
    
    if user.account_type == 'artist':
        try:
            profile = user.artist_profile
            form = ArtistProfileForm(instance=profile)
        except:
            form = ArtistProfileForm()
            
        if request.method == 'POST':
            form = ArtistProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = user
                profile.save()
                messages.success(request, 'Profile setup complete!')
                return redirect('dashboard')
                
    else:  # label
        try:
            profile = user.label_profile
            form = LabelProfileForm(instance=profile)
        except:
            form = LabelProfileForm()
            
        if request.method == 'POST':
            form = LabelProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = user
                profile.save()
                messages.success(request, 'Profile setup complete!')
                return redirect('dashboard')
    
    return render(request, 'accounts/profile_setup.html', {
        'form': form,
        'account_type': user.account_type
    })

@login_required
def dashboard(request):
    user = request.user
    context = {
        'user': user,
        'total_releases': 0,  # Will be populated with actual data
        'total_streams': 0,
        'total_earnings': 0,
        'recent_releases': [],
    }
    
    return render(request, 'accounts/dashboard.html', context)