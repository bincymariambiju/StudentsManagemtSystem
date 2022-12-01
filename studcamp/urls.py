from django.contrib import admin
from django.urls import path
from studcamp import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('contact_view', views.contact_view,name='contact_view'),
    path('adminlogin', views.adminlogin,name='adminlogin'),
    path('adminbase', views.adminbase,name='adminbase'),
    path('adminhome', views.adminhome,name='adminhome'),
    path('studentslogin', views.studentslogin,name='studentslogin'),
    path('studentbase', views.studentbase,name='studentbase'),
    path('studenthome', views.studenthome,name='studenthome'),
    path('signup', views.signup,name='signup'),
    path('signup_view', views.signup_view,name='signup_view'),
    path('delete/<int:id>',views.destroy,name='delete'),
    path('add_course', views.add_course,name='add_course'),
    path('course_view', views.course_view,name='course_view'),
    path('delete2/<int:id>',views.course_destroy,name='delete'),
    path('course_view2', views.course_view2,name='course_view2'),
    path('edit_course/<int:id>', views.edit_course,name="edit_course"),
    path('update_course/<int:id>',views.update_course,name='update_course'),
    path('staff', views.staff,name='staff'),
    path('staff_view', views.staff_view,name='staff_view'),
    path('edit_staff/<int:id>', views.edit_staff,name="edit_staff"),
    path('update_staff/<int:id>',views.update_staff,name='update_staff'),
    path('staff_view2', views.staff_view2,name='staff_view2'),
    path('delete1/<int:id>',views.staff_destroy,name='delete'),
    path('feedback', views.feedback,name='feedback'),
    path('feedback_view', views.feedback_view,name='feedback_view'),
    path('session', views.session,name='session'),
    path('session_view', views.session_view,name='session_view'),
    path('edit_session/<int:id>', views.edit_session,name="edit_session"),
    path('update_session/<int:id>',views.update_session,name='update_session'),
    
    path('session_view2', views.session_view2,name='session_view2'),
    path('delete3/<int:id>',views.destroy_session,name='delete'),
    
   
   

]
