from django.contrib import admin
from mysite.models import NewTable, Product
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','pub_date')

admin.site.register(NewTable)
admin.site.register(Product)