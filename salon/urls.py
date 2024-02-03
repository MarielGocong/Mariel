from django.urls import path
from.import views

urlpatterns = [
    path('',views.homePage, name="homePage"),
    path('about/', views.aboutPage, name="aboutPage"),
    path('createCustomer/', views.createCustomer, name="createCustomer"),
    path('deletebook/<int:pk>/', views.deleteBook, name="deleteBook"),
    path('updatecustomer/<int:pk>/', views.updateCustomer, name="updateCustomer"),
    path('viewcustomer/<int:pk>/', views.viewCustomer, name="viewCustomer"),
    path('viewHairInfo/<int:pk>/', views.viewHairInfo, name="viewHairInfo"),
    path('viewNailInfo/<int:pk>/', views.viewNailInfo, name="viewNailInfo"),
    path('addNailService/', views.addNailService, name="addNailService"),
    path('addHairService/', views.addHairService, name="addHairService"),
    path('addPackage/', views.addPackage, name="addPackage"),
    path('viewPackageInfo/<int:pk>/', views.viewPackageInfo, name="viewPackageInfo"),
    path('deleteHairService/<int:pk>/', views.deleteHairService, name="deleteHairService"),
    path('deletePackage/<int:pk>/', views.deletePackage, name="deletePackage"),
    path('deleteNailService/<int:pk>/', views.deleteNailService, name="deleteNailService"),
    path('updatePackage/<package_id>/', views.updatePackage, name="updatePackage"),
    path('updateHairService/<int:pk>/', views.updateHairService, name="updateHairService"),
    path('updateNailService/<int:pk>/', views.updateNailService, name="updateNailService"),
]