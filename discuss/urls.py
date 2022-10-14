from django.urls import path

from discuss import views

app_name = 'discuss'
urlpatterns = [
    path('addtitle/', views.AddTitle.as_view(), name='addtitle'),
    path('deletetitle/', views.DeleteTitle.as_view(), name='deletetitle'),
    path('addcomment/', views.AddComment.as_view(), name='addcomment'),
    path('deletecomment/', views.DeleteComment.as_view(), name='addcomment'),
    # path('queryall/', views.QueryAllTitle.as_view(), name='queryallTitle'),
    path('queryone/', views.QueryOneTitle.as_view(), name='queryoneTitle'),
    path('queryTitle/', views.QueryTitle.as_view(), name='queryTitle')
    # path('/queryAll', views..as_view(), name='login'),
]