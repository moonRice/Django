from django.contrib import admin
from .models import UserTypeHistory, UserLike


# Register your models here.
@admin.register(UserTypeHistory)
class UserTypeHistoryM(admin.ModelAdmin):
    list_display = (
        'user',
        'type',
        'count',
    )


@admin.register(UserLike)
class UserLikeM(admin.ModelAdmin):
    list_display = (
        'user',
        'result',
    )
