from django.urls import path
from django.contrib.auth import views as auth_views
from .views import supplierslist, addSupplier, supplierdetail, updatesupplier

urlpatterns = [
    path('supplierslist/', supplierslist, name='supplierslist' ),
    path('addsupplier/', addSupplier, name='addSupplier' ),
    path('supplierdetail/<str:pk>/', supplierdetail, name='supplierdetail' ),
    path('updatesupplier/<str:pk>/', updatesupplier, name='updatesupplier' ),

]
