from django.contrib import admin
from .models import SidebarMenuModel
from .models import DataForTableModel

# Register your models here.
class SidebarMenuAdmins(admin.ModelAdmin):
    list_display = ('title','table_title','link','pagename','relativepath','category','visibility')
    
admin.site.register(SidebarMenuModel, SidebarMenuAdmins)

class DataForTableAdmins(admin.ModelAdmin):
    list_display = ('title','desc','value','status')

admin.site.register(DataForTableModel, DataForTableAdmins)
