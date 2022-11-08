from django.shortcuts import render
from .models import Student
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    students = Student.objects.all()

    return render(request, 'index.html', {'students': students})

@csrf_exempt    
def add_student(request):
    body = json.loads(request.body)

    new_student = Student(name=body['name'], email=body['email'])
    new_student.save()
    
    return JsonResponse({'success': True})