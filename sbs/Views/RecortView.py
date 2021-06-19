
from datetime import timedelta, datetime
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from sbs.services import general_methods

from sbs.models.Highrecord import Highrecord
from sbs.Forms.HighRecortForm import HighRecortForm

@login_required
def return_recort(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    recort = Highrecord.objects.all()


    return render(request, 'Rekor/rekor.html', {'recort': recort})


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
    return render(request, 'Rekor/rekortEkle.html', {'recort_form': recort_form})

