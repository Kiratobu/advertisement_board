from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from app_employment.models import Vacancy

# Create your views here.

@permission_required('app_employment.view_vacancy')
def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render (request, 'employment/vacancy_list.html',{'vacancy_list':vacancies})