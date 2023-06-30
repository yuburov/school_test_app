from django.urls import path

from webapp.views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView, \
    StudentDetailView

app_name = 'webapp'

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('students/delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
]
