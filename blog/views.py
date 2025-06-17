import random
from dataclasses import dataclass

from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

def blog_list(request):
    posts = Blog.objects.all()
    return render(request,'blog/base.html', {'posts': posts})


# @dataclass
# class Student:
#     first_name: str
#     last_name: str
#     phone: str
#     payed: bool
#
# st1 = Student("Alex", "Garden", "99 123 23 56", True)
# st2 = Student("Ali", "Toshmat", "88 876 23 56", True)
# st3 = Student("Vali", "Eshmat", "77 198 65 56", False)
# students = [st1, st2, st3]
#
# def home(request):
#     a = random.randint(1, 100)
#     b = random.randint(101, 1000)
#     c = a + b
#     context = {
#         "a": a,
#         "b": b,
#         "c": c,
#         "students": students
#     }
#     return render(request, 'blog/base.html', context=context)



