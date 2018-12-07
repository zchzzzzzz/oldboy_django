from django.shortcuts import render, HttpResponse
import time


def show_time(request):
    t1 = time.ctime()
    return render(request, "index.html", {"time1": t1})
