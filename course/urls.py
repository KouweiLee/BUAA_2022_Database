from django.urls import path

from course import views

app_name = 'class'
urlpatterns = [
    path('course/all/', views.GetAllCourses.as_view(), name='getallcourse'),
    path('course/addone/', views.AddCourse.as_view(), name='addOneCourse'),
    path('course/single/', views.ClickCourse.as_view(), name='clickCourse'),
    path('course/change/', views.ChangeCourse.as_view(), name='changeCourse'),
    path('course/delete/', views.DeleteCourse.as_view(), name='deleteCourse'),
    path('work/all/', views.GetAllWorks.as_view(), name='getallwork'),
    path('work/single/', views.ClickWork.as_view(), name='clickWork'),
    path('work/addone/', views.AddWork.as_view(), name='addWork'),
    path('work/change/', views.ChangeWork.as_view(), name='changeWork'),
    path('work/delete/', views.DeleteWork.as_view(), name='deleteWork'),
]