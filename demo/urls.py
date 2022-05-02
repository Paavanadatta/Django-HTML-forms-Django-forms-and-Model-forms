
import django


from django.urls import path
from demo import views
urlpatterns=[
    path('register/',views.register,name="register"),
    path('update/<pk>/',views.update,name="update"),
    path('select/',views.select,name="select"),
    path('delete/<pk>/',views.delete,name="delete")
]