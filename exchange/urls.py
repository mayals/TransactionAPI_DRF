from django.urls import path
from . import views

urlpatterns = [
    # Category
    path('CategoryListCreate/', views.CategoryListCreateAPIView.as_view(),name='CategoryListCreate'),
    path('CategoryRetrieveUpdateDestroy/<int:pk>/',views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='CategoryRetrieveUpdateDestroy'),


    # Currency
    path('CurrencyListCreate/', views.CurrencyListCreateAPIView.as_view(),name='CurrencyListCreate'),
    path('CurrencyRetrieveUpdateDestroy/<int:pk>/',views.CurrencyRetrieveUpdateDestroyAPIView.as_view(), name='CurrencyRetrieveUpdateDestroy'),


    # Transaction
    path('transaction_list/', views.transaction_list,name='transaction_list'),
    path('transaction_detail/<int:pk>/',views.transaction_detail, name='transaction_detail'),
   
]

