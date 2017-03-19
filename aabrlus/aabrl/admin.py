from django.contrib import admin
from aabrl.models import Urls
# Register your models here.
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('encurt_id','url_original','pub_date', 'contador')
    ordering = ('-pub_date',)
 
admin.site.register(Urls, UrlsAdmin)
