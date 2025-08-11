from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ArtistProfile, LabelProfile

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'account_type', 'plan', 'is_verified', 'created_at')
    list_filter = ('account_type', 'plan', 'is_verified', 'created_at')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('account_type', 'plan', 'phone_number', 'country', 'bio', 'profile_image', 'is_verified')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ArtistProfile)
admin.site.register(LabelProfile)