from django.urls import path
from demo3 import views
app_name='demo3'

urlpatterns=[
    path('enq/', views.enqview ,name='enq'),
    path('update/<pk>/',views.updateenqview,name='update'),
    path('select/', views.selectenqview ,name='select'),
    path('delete/<pk>/', views.deleteenqview ,name='delete'),
    path('download/', views.download_csv ,name='download'),


]
