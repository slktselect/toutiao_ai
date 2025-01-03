from django.contrib import admin

from toutiao_user.models import TTUser

class TTUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'cookie', 'phone', 'password', 'user_agent')
    search_fields  = ('name', 'phone')
    list_filter   = ()
    readonly_fields = ('id',)

# Register your models here.
admin.site.register(TTUser, TTUserAdmin)