from django.urls import path

from announce import views

app_name = 'announce'
urlpatterns = [
    path('develop/all/', views.GetAllDevelops.as_view(), name='addtitle'),
]