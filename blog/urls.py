from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"

urlpatterns = [
    path('blogs/', views.blogs, name = "blogs"),
    path("single/<int:id>/", views.single, name = "single"),
    path("category/<str:category>/", views.category, name = "category"),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)