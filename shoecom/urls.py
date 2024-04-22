"""
URL configuration for shoecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from view import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('view_product/', views.view_product, name='view_product'),
    path('login/', views.login, name='loginx'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('handle_login/', views.handle_login, name='handle_login'),
    path('handle_signup/', views.handle_signup, name='handle_signup'),
    path('order_now/', views.order_now, name='order_now'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('add_cart/', views.add_cart, name='add_cart'),
    path('cart/', views.mycart, name='cart'),
    path('handle_cart/', views.handle_cart, name='handle_cart'),
    path('edit_cart_item/', views.edit_cart_item, name='edit_cart_item'),
    path('handle_edit_cart_item/', views.handle_edit_cart_item, name='handle_edit_cart_item'),
    path('delete_cart_item/', views.delete_cart_item, name='delete_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('handle_checkout/', views.handle_checkout, name='handle_checkout'),
    path('order_now_cart/', views.order_now_cart, name='order_now_cart'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)