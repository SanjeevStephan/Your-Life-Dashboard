from django.urls import path
from . import views

urlpatterns = [
    path('', views.MASTER_CATEGORY_VIEW, name='MASTER_CATEGORY_VIEW'),
    path('menu/<pk>', views.PREVIEW_CONTENT_VIEW, name='PREVIEW_CONTENT_VIEW')
]