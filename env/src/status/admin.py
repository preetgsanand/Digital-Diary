from django.contrib import admin
from .models import Status
# Register your models here.

class StatusAdmin(admin.ModelAdmin):
	class Meta:
		model = Status
	list_display = ["username","timestamp"];
	list_filter = ["timestamp","updated"];

admin.site.register(Status,StatusAdmin)
