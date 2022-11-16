from django.urls import path

from announce import views

app_name = 'announce'
urlpatterns = [
    path('develop/all/', views.GetAllDevelops.as_view(), name='addtitle'),
    path('develop/add/', views.AddDevelop.as_view(), name='addtitle'),
    path('develop/change/', views.ChangeDevelop.as_view(), name='addtitle'),
]