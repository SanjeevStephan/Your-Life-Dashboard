from django.db import models

# Create your models here.
class SidebarMenuModel(models.Model):
    title = models.CharField(max_length=200)
    table_title = models.CharField(max_length=200,default='Default Table Title')
    link  = models.CharField(max_length=200)
    icon  = models.CharField(max_length=200, default='bi bi-file-earmark')
    category = models.CharField(max_length=200, default='test')
    relativepath = models.CharField(max_length=250, default='Home/Server')
    pagename = models.CharField(max_length=250,default='pages/empty.html')
    visibility = models.CharField(max_length=100, default='show')

class DataForTableModel(models.Model):
    title = models.CharField(max_length=250, default='Default Title')
    desc  = models.CharField(max_length=250,null=True,blank=True)
    value = models.CharField(max_length=250,null=True,blank=True)
    category = models.CharField(max_length=200, default='test')
    status = models.CharField(max_length=200,default='success')