from django.shortcuts import render
from django.http import HttpResponse
from math import pi

# Create your views here.
def get_rectangle_area(request, width, height):
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width):
    return render(request, 'geometry/square.html')


def get_circle_area(request, radius):
    return render(request, 'geometry/circle.html')



