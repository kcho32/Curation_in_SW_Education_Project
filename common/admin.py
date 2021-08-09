from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin
from .models import CustomUser, CustomerMessage, NewsAgreedCustomer
from .forms import UserCreationForm


class UserAdmin(UserBaseAdmin):
    add_form = UserCreationForm

    list_display = ('username', 'email', 'self_prove', 'self_prove_answer', 'is_active',
                    'is_staff', 'is_superuser', 'date_joined')
    fieldsets = (
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Account Info', {'fields': ('username', 'password', 'self_prove', 'self_prove_answer', 'date_joined')}),
        ('Status', {'fields': ('is_staff', 'is_superuser', 'is_active')})
    )
    list_filter = ('is_staff', 'is_superuser')


admin.site.register(CustomUser, UserAdmin)
admin.site.register(CustomerMessage)
admin.site.register(NewsAgreedCustomer)

