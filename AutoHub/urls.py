from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('cars/', views.car_list, name='car_list'),
    path('manufacturers/', views.manufacturer_list, name='manufacturer_list'),
    path('sellers/', views.seller_list, name='seller_list'),
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),
    path('manufacturers/<int:pk>/', views.manufacturer_detail, name='manufacturer_detail'),
    path('sellers/<int:pk>/', views.seller_detail, name='seller_detail'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)