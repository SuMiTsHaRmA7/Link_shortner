from django.contrib import admin
from django.urls import path
from link import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path("developer", views.developer, name = "developer")

]