from django.contrib import admin
from accounts.models import (CustomUser, PhoneNumber, Profile,
                         EmailSubscibers, BestCustomerReviews)
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'is_superuser',
                'is_staff',
                'is_merchant',
                'is_customer',
                'is_blogger',
            ),
        }),
    )
    
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PhoneNumber)
admin.site.register(Profile)
admin.site.register(EmailSubscibers)
admin.site.register(BestCustomerReviews)
