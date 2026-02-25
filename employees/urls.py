from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_list,name='employee_list'),
    path('/<int:id>/',views.get_employee_detail,name="employee_detail"),
    path('/create/',views.employee_create,name="employee_create"),
    path('/update/<int:id>/',views.employee_update,name="employee_update"),
]