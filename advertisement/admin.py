from pyexpat import model
from django.contrib import admin

from advertisement.models import Advertisement,Author




@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']





@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name']
    search_fields = ['first_name','last_name']
    fieldsets = (
        ('Основные сведения',{
            'fields':('name','first_name','last_name')
        }),
        ('Биографические данные',{
            'fields':('birth_date','biography'),
            'classes':['collapse']
        }),
        ('Контакты',{
            'fields':('instagram','email','twitter')})
    )
# Register your models here.
