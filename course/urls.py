from django.urls import path

from course import views_Course, views_Work

app_name = 'class'
urlpatterns = [
    path('course/all/', views_Course.GetAllCourses.as_view(), name='getallcourse'),
    path('course/addone/', views_Course.AddCourse.as_view(), name='addOneCourse'),
    path('course/single/', views_Course.ClickCourse.as_view(), name='clickCourse'),
    path('course/change/', views_Course.ChangeCourse.as_view(), name='changeCourse'),
    path('course/delete/', views_Course.DeleteCourse.as_view(), name='deleteCourse'),
    path('course/choose/', views_Course.ChooseCourse.as_view(), name='chooseCourse'),
    path('work/all/', views_Work.GetAllWorks.as_view(), name='getallwork'),
    path('work/single/', views_Work.ClickWork.as_view(), name='clickWork'),
    path('work/addone/', views_Work.AddWork.as_view(), name='addWork'),
    path('work/change/', views_Work.ChangeWork.as_view(), name='changeWork'),
    path('work/delete/', views_Work.DeleteWork.as_view(), name='deleteWork'),
    path('work/upload/', views_Work.UploadWork.as_view(), name='uploadWork'),
    path('work/correcting/', views_Work.CorrectWorks.as_view(), name='correctWork'),
    path('work/deleteRecord/', views_Work.DeleteWorkRecord.as_view(), name='deleteWorkRecord'),
    path('work/score/', views_Work.GiveScore2Work.as_view(), name='giveScore2Work'),
    path('work/downloadOne/', views_Work.DownloadOne.as_view(), name='giveScore2Work'),
    path('attachment/all/', views_Course.GetAllAttachments.as_view(), name='getAllAttachments'),
    path('attachment/upload/', views_Course.UploadAttachment.as_view(), name='UploadAttachment'),
    path('attachment/delete/', views_Course.DeleteAttachment.as_view(), name='DeleteAttachment'),
]