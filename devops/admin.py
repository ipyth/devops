from django.contrib import admin
from .models import User, Host, Services

# Register your models here.


class HostAdmin(admin.ModelAdmin):
	list_display = [
		'hostname',
		'ip',
		'type',
		'os',
		'note',
	]

admin.site.register(User)
admin.site.register(Host, HostAdmin)
admin.site.register(Services)
