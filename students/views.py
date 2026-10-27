from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.db.models import Q


def students_home(request):
    error = None

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("students_home")
    else:
        form = StudentForm()

    search_query = request.GET.get("search", "")

    students = Student.objects.all()

    if search_query:
        students = students.filter(
            Q(name__icontains=search_query) |
            Q(course__icontains=search_query)
        )

        if search_query.isdigit():
            students = students | Student.objects.filter(
                age=int(search_query)
            )

    return render(request, "home.html", {
        "students": students,
        "form": form,
        "error": error,
        "search_query": search_query
    })
def update_student(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("students_home")

    else:
        form = StudentForm(instance=student)

    return render(request, "update_student.html", {
        "form": form,
        "student": student
    })


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        return redirect("students_home")

    return render(request, "delete_student.html", {
        "student": student
    })