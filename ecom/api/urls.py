from django.urls import path,include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('',home ,name='api.home'),
    path('category/',include('api.category.urls'),name ="category"),
    path('products/',include('api.product.urls'),name ="products"),
    path('users/',include('api.user.urls'),name ="users"),
    path('orders/',include('api.order.urls'),name ="orders"),
    path('payments/',include('api.payment.urls'),name ="payments"),

    path('api-token-auth/',views.obtain_auth_token,name='api_token_auth')

]