from django.urls import path
from demo2 import views
urlpatterns=[
    path('register/',views.registerview,name="register"),
    path('update/<pk>/',views.updateview,name="update"),
    path('select/',views.selectview,name="select"),
    path('delete/<pk>/',views.deleteview,name="delete")
]

