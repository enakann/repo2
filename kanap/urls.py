
from django.urls import path,include
from kanap import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    #path('kan/',include('kanap.urls.py')),

    
]
