from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "credits"

urlpatterns = [
    path('credits/', views.credits, name = "credits"),
    path("single/<int:id>/", views.single, name = "single"),
    path("category/<str:category>/", views.category, name = "category"),
    
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)