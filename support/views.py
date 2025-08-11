from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def support_center(request):
    return render(request, 'support/center.html')

@login_required
def create_ticket(request):
    return render(request, 'support/create_ticket.html')