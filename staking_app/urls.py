
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from staking_app import views 

# from .views import load_new_user,load_points_table


urlpatterns = [
    # admin
    path('', views.index,name='index'),
    # ------mmmmmmmmm-------------- 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
