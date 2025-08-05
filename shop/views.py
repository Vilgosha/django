from django.shortcuts import render
from django.http import HttpResponse
# from . import models
from .models import Course


# Create your views here.


# def index(request):
#     return HttpResponse("Hello from the Shop app")


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})
    # return HttpResponse(courses)
    # return HttpResponse(''.join([str(course) + '<br>' for course in courses]))


# models.Course
# models.Category
