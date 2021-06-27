
from datetime import timedelta, datetime
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from sbs.Forms.HighRecordSearchForm import HighRecortSearchForm
from sbs.services import general_methods

from sbs.models.Highrecord import Highrecord
from sbs.Forms.HighRecortForm import HighRecortForm
from django.contrib import messages

@login_required
def return_recort(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    recort = None
    recort_form=HighRecortSearchForm()

    if request.method == 'POST':

        recort_form = HighRecortSearchForm(request.POST)
        if recort_form.is_valid():
            name = recort_form.cleaned_data.get('name')
            siklet = recort_form.cleaned_data.get('weight')
            recordtype = recort_form.cleaned_data.get('recordtype')
            ages = recort_form.cleaned_data.get('agecategory')
            recordwhich = recort_form.cleaned_data.get('recordwhich')
            competition = recort_form.cleaned_data.get('competition')

            if not (name or siklet or recordtype == None or ages or recordwhich == None or competition):
                recort = Highrecord.objects.all()
            else:
                query = Q()
                if name:
                    query &= Q(name__icontains=name)
                if siklet != None:
                    query &= Q(weight=siklet)
                if recordtype != None:
                    query &= Q(recordtype=recordtype)
                if ages != None:
                    query &= Q(agecategory=ages)
                if recordwhich != None:
                    query &= Q(recordwhich=recordwhich)
                if competition:
                    query &= Q(competition=competition)
                recort = Highrecord.objects.filter(query)

    return render(request, 'Rekor/rekor.html', {'recort': recort,'recort_form':recort_form})


def return_newRecort(request,):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    recort_form=HighRecortForm()
    if request.method == 'POST':
        recort_form=HighRecortForm(request.POST)
        if recort_form.is_valid():
            recort_form.save()
            return redirect('sbs:rekor-listesi')
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'Rekor/rekortEkle.html', {'recort_form': recort_form})


def return_updateRecort(request,pk ):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    rekor=Highrecord.objects.get(pk=pk)
    recort_form = HighRecortForm(request.POST or None, instance=rekor )
    if request.method == 'POST':
        if recort_form.is_valid():
            recort_form.save()
        return redirect('sbs:rekor-listesi')
    return render(request, 'Rekor/rekorGuncelle.html', {'recort_form': recort_form})

