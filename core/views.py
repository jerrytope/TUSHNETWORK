from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def pricing(request):
    plans = [
        {
            'name': 'Artiste Plan',
            'price': '₦5,000',
            'period': 'per release',
            'features': [
                'Distribute to 200+ platforms',
                'Keep 100% of royalties',
                'Basic analytics',
                'SmartLinks',
                'Email support',
            ]
        },
        {
            'name': 'Artist Plus',
            'price': '₦15,000',
            'period': 'per month',
            'features': [
                'Everything in Artiste Plan',
                'Unlimited releases',
                'Advanced analytics',
                'Pre-save campaigns',
                'Playlist pitching',
                'PR services',
                'Priority support',
                'YouTube monetization',
            ]
        }
    ]
    
    return render(request, 'core/pricing.html', {'plans': plans})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')