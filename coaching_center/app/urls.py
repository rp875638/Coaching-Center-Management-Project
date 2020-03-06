from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.signin,name='signin'),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('registerpage',views.registerpage,name="registerpage"),
    path('<int:id>/save',views.save,name='save'),
    path('<int:id>/save_detail',views.save_detail,name='save_detail'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('<int:id>/setting',views.setting,name='setting'),
    path('<int:id>/profile',views.profile,name='profile'),
    path('<int:id>/fees',views.fees,name="fees"),
    path('add_fees',views.add_fees,name="add_fees"),
    path('<int:id>/batch',views.batch,name="batch"),
    path('add_batch',views.add_batch,name="add_batch"),
    path('<str:types>/<int:id>/delete_notification',views.delete_notification,name="delete_notification"),
    path('<int:id>/notification',views.notification,name="notification"),
    path('add_notification',views.add_notification,name="add_notification"),
    path('<int:id>/tests',views.tests,name="tests"),
    path('add_tests',views.add_tests,name="add_tests"),
    path('setting',views.setting,name='setting'),
    path('<int:id>/salary',views.salary,name="salary"),
    path('add_salary',views.add_salary,name="add_salary"),
    path('<int:id>/teachers',views.teachers,name="teachers"),
    path('<int:id>/students',views.students,name="students"),
    path('<int:id>/result',views.results,name="result"),
    path('add_results',views.add_results,name="add_results"),
    path('attendence',views.attendence,name="attendence"),
    path('t_attendence',views.t_attendence,name="t_attendence"),
    path('<int:id>/take_attendence',views.take_attendence,name="take_attendence"),
    path('s_attendence',views.s_attendence,name="s_attendence"),
    path('<int:id>/assignment',views.assignments,name="assignment"),
    path('add_assignments',views.add_assignments,name="add_assignments"),
    path('<str:types>/<int:id>/details',views.details,name="details"),
    path('<int:id>/accept',views.accept,name="accept"),
]