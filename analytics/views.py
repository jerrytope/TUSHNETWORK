from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count
from .models import RoyaltyReport, Withdrawal
from distribution.models import Release
from datetime import datetime, timedelta

@login_required
def analytics_dashboard(request):
    user = request.user
    releases = Release.objects.filter(user=user)
    
    # Get analytics data for user's releases
    release_stats = []
    for release in releases[:10]:  # Show top 10 releases
        streams = RoyaltyReport.objects.filter(
            user=user, release=release
        ).aggregate(total=Sum('streams'))['total'] or 0
        
        earnings = RoyaltyReport.objects.filter(
            user=user, release=release
        ).aggregate(total=Sum('earnings'))['total'] or 0
        
        release_stats.append({
            'release': release,
            'streams': streams,
            'earnings': earnings
        })
    
    context = {
        'releases': releases,
        'release_stats': release_stats,
        'total_releases': releases.count()
    }
    
    return render(request, 'analytics/dashboard.html', context)

@login_required
def royalties(request):
    user = request.user
    
    # Get total earnings
    total_earnings = RoyaltyReport.objects.filter(user=user).aggregate(
        total=Sum('earnings')
    )['total'] or 0
    
    # Get total streams
    total_streams = RoyaltyReport.objects.filter(user=user).aggregate(
        total=Sum('streams')
    )['total'] or 0
    
    # Get recent royalty reports
    recent_reports = RoyaltyReport.objects.filter(user=user).order_by('-report_date')[:10]
    
    # Get withdrawal history
    withdrawals = Withdrawal.objects.filter(user=user).order_by('-requested_at')[:5]
    
    # Calculate available balance
    withdrawn = Withdrawal.objects.filter(
        user=user, status='completed'
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    available_balance = total_earnings - withdrawn
    
    context = {
        'total_earnings': total_earnings,
        'total_streams': total_streams,
        'recent_reports': recent_reports,
        'withdrawals': withdrawals,
        'available_balance': available_balance
    }
    
    return render(request, 'analytics/royalties.html', context)

@login_required
def request_withdrawal(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        bank_name = request.POST.get('bank_name')
        account_number = request.POST.get('account_number')
        account_name = request.POST.get('account_name')
        
        # Calculate available balance
        total_earnings = RoyaltyReport.objects.filter(user=request.user).aggregate(
            total=Sum('earnings')
        )['total'] or 0
        
        withdrawn = Withdrawal.objects.filter(
            user=request.user, status='completed'
        ).aggregate(total=Sum('amount'))['total'] or 0
        
        available_balance = total_earnings - withdrawn
        
        if float(amount) <= available_balance and float(amount) >= 1000:  # Minimum ₦1000
            withdrawal = Withdrawal.objects.create(
                user=request.user,
                amount=amount,
                bank_details={
                    'bank_name': bank_name,
                    'account_number': account_number,
                    'account_name': account_name
                }
            )
            messages.success(request, 'Withdrawal request submitted successfully!')
        else:
            messages.error(request, 'Invalid withdrawal amount. Minimum is ₦1000.')
    
    return redirect('royalties')