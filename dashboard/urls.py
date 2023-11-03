from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('grocery/', views.grocery, name='dashboard-grocery'),
    path('inventory/', views.inventory, name='dashboard-inventory'),
    path('inventory/delete/<int:pk>/', views.product_delete, name='dashboard-inventory-delete'),
    path('grocery/purchased/<int:pk>/', views.product_purchased, name='dashboard-grocery-purchased'),
    path('inventory/update/<int:pk>/', views.product_update, name='dashboard-inventory-update'),
    path('grocery/update/<int:pk>/', views.product_edit, name='dashboard-grocery-edit'),
]
