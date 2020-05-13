from itertools import combinations

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from sbs.Forms.CompetitionForm import CompetitionForm
from sbs.Forms.CompetitionSearchForm import CompetitionSearchForm
from django.db.models import Q
from sbs.models import SportClubUser, SportsClub, Competition, Athlete, CompAthlete, Weight
from sbs.models.ReferenceReferee import ReferenceReferee
from sbs.models.ReferenceCoach import ReferenceCoach
from sbs.models.ReferenceAthlete import ReferenceAthlete
from sbs.models.SimpleCategory import SimpleCategory
from sbs.models.EnumFields import EnumFields
from sbs.services import general_methods

from datetime import date, datetime
from django.utils import timezone


@login_required
def hakemler(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    referee = ReferenceReferee.objects.all()
    return render(request, 'basvurular/hakembasvuru.html', {'referees': referee})


@login_required
def antroner(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    referee = ReferenceCoach.objects.all()
    return render(request, 'basvurular/antrenorbasvuru.html', {'referees': referee})


@login_required
def sporcular(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    referee = ReferenceAthlete.objects.all()
    return render(request, 'basvurular/sporcubasvuru.html', {'referees': referee})
