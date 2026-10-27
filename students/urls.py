from django.urls import path
from . import views

urlpatterns = [
    path("", views.students_home, name="students_home"),
    path("update/<int:student_id>/", views.update_student, name="update_student"),
    path(
    "delete/<int:student_id>/",
    views.delete_student,
    name="delete_student"
),
]