from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
	list_display = ["highlight","photo"]
	list_filter = ["date","updated"]
	class Meta:
		model = Page

admin.site.register(Page,PageAdmin)
