from django.shortcuts import render
from datetime import date
import calendar


def index(request):
    d = date.today()
    x = calendar.day_name[d.weekday()]
    return render(request, "wednesday/index.html", {
        "wednesday": x == "Wednesday"
    })