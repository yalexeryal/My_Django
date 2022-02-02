from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

days_dict = {
    'monday': "список дел запланированных на понедельник",
    'tuesday': "список дел запланированных на вторник",
    'wednesday': "список дел запланированных на среду",
    'thursday': "список дел запланированных на четверг",
    'friday': "список дел запланированных на пятницу",
    'saturday': "список дел запланированных на субботу",
    'sunday': "список дел запланированных на воскресения",
}


def get_info_about_sing_days(request, sing_days):
    return render(request, 'week_days/greeting.html')

def get_info_about_sing_days_by_number(request, sing_days):
    days = list(days_dict)
    if sing_days > len(days):
        return HttpResponse(f"Неверный номер дня - {sing_days}")
    name_days = days[sing_days - 1]
    redirect_url = reverse('days-name', args=(name_days,))
    return HttpResponseRedirect(redirect_url)

