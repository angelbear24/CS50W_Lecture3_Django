from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    return render(request, "newyear/index.html", {
        "newyear": date.month ==1 and date.day == 1
    })