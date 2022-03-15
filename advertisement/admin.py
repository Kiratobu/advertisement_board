from django.contrib import admin

from advertisement.models import Advertisement




@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
# Register your models here.
