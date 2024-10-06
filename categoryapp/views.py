import re
from django.utils import timezone
from django.shortcuts import render
from .models import SidebarMenuModel as sidebar
from .models import DataForTableModel as datafortable
from tracker.models import FeelingLogsModel as feelinglogs
from tracker.models import MonitorActivityDataModel as monitordata
from tracker.models import PersonalIdeasBankModel as ideasbank
from .models import DataForTableModel as tabledata
# Create your views here.

# Get Today's Date
today = timezone.now().date()
todays_todo_list = monitordata.objects.filter(deadline=today).order_by('deadline')


context = {
    'sidebar' : sidebar.objects.all(),
    'datafortable' : datafortable.objects.all(),
    'feelinglogs' : feelinglogs.objects.order_by('datetime'),
    'monitordata' : monitordata.objects.order_by('datetime'),
    'ideasbank'   : ideasbank.objects.all(),
    'todays_todolist'    : todays_todo_list,
    'breadcrumb' : ['Home', 'Dashboard'],
    'website_title' : "Your Life's Dashboard"
}




def MASTER_CATEGORY_VIEW(request):
    return render(request, 'index.html', context)

def PREVIEW_CONTENT_VIEW(request, pk):
    context_data = sidebar.objects.get(pk=pk)
    content_title = context_data.title
    page_name = f"{'pages/'}{context_data.pagename}.html" # => /pages/monitor_projects.html
    table_title = context_data.table_title
    breadcrumb_list = re.split('/',context_data.relativepath)
    context.update({ 'breadcrumb' : breadcrumb_list }) 
    context['heading'] = content_title
    context['title'] = table_title 
    context['page'] = page_name
    return render(request, 'preview.html', context)

