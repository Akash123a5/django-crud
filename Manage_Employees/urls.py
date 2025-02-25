from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage_employees, name='home'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('edit_employee/<int:id>/', views.edit_employee, name='edit_employee'),
    path('update_employee/<int:id>/', views.update_employee, name='update_employee'),
    path('delete_employee/<int:id>/', views.delete_employee, name='delete_employee'),
    path('delete_all/', views.delete_all, name='delete_all'),
]
