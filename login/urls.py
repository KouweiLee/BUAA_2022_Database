from django.urls import path

from login import views

app_name = 'login'
urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('changepw/', views.ChangePassWord.as_view(), name='changepw'),
    path('upload/', views.UploadHeader.as_view(), name='uploadHeader'),
    path('picture/all/', views.GetAllPics.as_view(), name='getAllPics'),
    path('picture/upload/', views.AddPic.as_view(), name='getAllPics'),
    path('picture/delete/', views.DeletePic.as_view(), name='getAllPics'),
]