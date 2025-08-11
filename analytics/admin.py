from django.contrib import admin
from .models import RoyaltyReport, Withdrawal

@admin.register(RoyaltyReport)
class RoyaltyReportAdmin(admin.ModelAdmin):
    list_display = ('release', 'platform', 'streams', 'earnings', 'report_date')
    list_filter = ('platform', 'report_date')

@admin.register(Withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'requested_at')
    list_filter = ('status', 'requested_at')