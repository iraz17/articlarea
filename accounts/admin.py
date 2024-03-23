from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
from articles.models import Category

class AccountAdmin(UserAdmin):
    list_display = ('email', 'firstname', 'lastname', 'username', 'last_login', 'date_joined', 'is_active')
    list_disply_links = ('email', 'firstname', 'lastname')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined', )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)


admin.site.register(Category)