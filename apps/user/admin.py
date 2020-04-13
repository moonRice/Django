from django.contrib import admin
from .models import User, Address

import options49

admin.site.site_title = options49.my_site_title
admin.site.site_header = options49.my_site_header
admin.site.index_title = options49.my_index_title


@admin.register(User)
class UserControl(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'is_active',
    )


@admin.register(Address)
class AddrControl(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'receiver',
        'addr',
        'zip_code',
        'phone',
        'is_default',
    )

