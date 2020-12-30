from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from sbs.Forms.ClaimForm import ClaimForm
from sbs.services import general_methods
from sbs.models.Claim import Claim


@login_required
def return_claim(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    destek = Claim.objects.all()
    return render(request, 'Destek/DestekTalepListesi.html', {'claim': destek,})

    # if request.method == 'POST':

        # user_form = UserSearchForm(request.POST)
        # firstName = request.POST.get('first_name')
        # lastName = request.POST.get('last_name')
        # email = request.POST.get('email')
        # playDate=request.POST.get('playDate')
        # finishDate=request.POST.get('finishDate')
        # if playDate:
        #     playDate = datetime.strptime(playDate, '%d/%m/%Y').date()
        #
        # if finishDate:
        #     finishDate=datetime.strptime(finishDate, "%d/%m/%Y").date()
        #
        # if not (firstName or lastName or email or playDate or finishDate):
        #     logs = Logs.objects.all().order_by('-creationDate')
        #
        # else:
        #     query = Q()
        #     if lastName:
        #         query &= Q(user__last_name__icontains=lastName)
        #     if firstName:
        #         query &= Q(user__first_name__icontains=firstName)
        #     if email:
        #         query &= Q(user__email__icontains=email)
        #     if playDate:
        #         query &= Q(creationDate__gte = playDate)
        #     if finishDate:
        #         query &= Q(creationDate__lt = finishDate)
        #


            # logs = Logs.objects.filter(query).order_by('-creationDate')




@login_required
def claim_add(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    claim_form = ClaimForm()

    if request.method == 'POST':
        claim_form=ClaimForm(request.POST)
        if claim_form.is_valid():
            claim_form.save()
            messages.success(request, 'Destek Talep  Eklendi.')

    return render(request, 'Destek/Desktek-ekle.html', {'claim_form': claim_form, })


@login_required
def claim_update(request,pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    clain=Claim.objects.get(pk=pk)
    claim_form = ClaimForm(request.POST or None, instance=clain)

    if request.method == 'POST':
        if claim_form.is_valid():
            claim_form.save()
            messages.success(request, 'Destek Talep  Güncellendi.')

    return render(request, 'Destek/Desktek-ekle.html', {'claim_form': claim_form, })





@login_required
def claim_delete(request,pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')

    clain=Claim.objects.get(pk=pk)
    clain.delete()

    messages.success(request, 'Destek Talep  Silindi.')

    return redirect('sbs:destek-talep-listesi')