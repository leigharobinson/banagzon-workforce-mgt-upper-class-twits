from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from hrapp import views
from .views import *
from hrapp.models import departments

app_name = 'hrapp'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('employees/<int:employee_id>/', employee_details, name='employee'),
    path('employees/employee_form', employee_form, name='employee_form'),
    path('employees/<int:employee_id>/employee_form/', employee_edit_form, name='employee_edit_form'),
    path('departments/', department_list, name='department_list')
]
