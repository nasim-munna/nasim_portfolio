from django.urls import path
from . import views
app_name = 'portfolio'
urlpatterns = [
    path('', views.home,name='home'),
    path('blog/<slug>/', views.blog_details, name='blog_details'),
    
    
]