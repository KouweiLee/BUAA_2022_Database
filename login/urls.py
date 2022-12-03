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
    path('user/changeName/', views.ChangeName.as_view(), name='getAllPics'),
    path('user/changeProfile/', views.ChangeProfile.as_view(), name='getAllPics'),
    path('user/changeSuper/', views.ChangeSuper.as_view(), name='getAllPics'),
    path('user/setphoto/', views.SetPhoto.as_view(), name='getAllPics'),
    path('user/getphoto/', views.GetPhoto.as_view(), name='getAllPics'),
    path('user/getprofile/', views.GetProfile.as_view(), name='getAllPics'),
]