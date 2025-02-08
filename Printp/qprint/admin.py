from django.contrib import admin
from .models import College, PrintingShop

# Register your models here.
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PrintingShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'college')
    search_fields = ('name', 'college__name')
    list_filter = ('college',)

admin.site.register(College, CollegeAdmin)
admin.site.register(PrintingShop, PrintingShopAdmin)
