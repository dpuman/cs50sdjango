from django.shortcuts import render
import datetime


def index(request):
    now = datetime.datetime.now()
    return render(request, 'newyear/index.html', {'date': now.date == 1 and now.month == 1})
# now.date == 1 and now.month == 1
