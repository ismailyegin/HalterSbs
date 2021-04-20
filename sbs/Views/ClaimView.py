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
from sbs.Forms.UserSearchForm import UserSearchForm
from sbs.Forms.ClaimAdminForm import  ClaimAdminForm
from sbs.services import general_methods
from sbs.models.Claim import Claim


from sbs.models.File import File



from sbs.models import MenuDirectory,MenuAdmin




@login_required
def return_claim(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    user_form = UserSearchForm()
    claim_form=ClaimAdminForm()
    destek = Claim.objects.none()
    if request.method == 'POST':
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        email = request.POST.get('email')
        status = request.POST.get('status')
        importanceSort = request.POST.get('importanceSort')
        project = request.POST.get('project')
        if not (firstName or lastName or email or status or importanceSort or project):
            destek = Claim.objects.all()
        else:
            query = Q()
            if lastName:
                query &= Q(user__last_name__icontains=lastName)
            if firstName:
                query &= Q(user__first_name__icontains=firstName)
            if email:
                query &= Q(user__email__icontains=email)
            if importanceSort:
                query &= Q(importanceSort=importanceSort)
            if status:
                query &= Q(status=status)
            if project:
                query &= Q(project=project)
            destek = Claim.objects.filter(query)
    return render(request, 'Destek/DestekTalepListesi.html' , {'claims': destek.order_by('-creationDate'),
                                                               'user_form':user_form,
                                                               'claim_form':claim_form
                                                               })


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
            claim=claim_form.save(commit=False)
            claim.user=request.user
            claim.save()
            if request.FILES.getlist('files'):
                for item in request.FILES.getlist('files'):
                    evrak = File(file=item)
                    evrak.save()
                    claim.files.add(evrak)
                    claim.save()

            messages.success(request, 'Deste-Talep  Başarı ile Eklendi. ')
            return redirect('sbs:destek-talep-listesi')

    return render(request, 'Destek/Desktek-ekle.html', {'claim_form': claim_form, })


@login_required
def claim_update(request,pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    clain=Claim.objects.get(pk=pk)
    claim_form = ClaimAdminForm(request.POST or None, instance=clain)

    if request.method == 'POST':
        if claim_form.is_valid():
            claim=claim_form.save(commit=False)
            claim.save()
            if request.FILES.getlist('files'):
                for item in request.FILES.getlist('files'):
                    evrak = File(file=item)
                    evrak.save()
                    claim.files.add(evrak)
                    claim.save()
            messages.success(request, 'Destek Talep  Güncellendi.')
    return render(request, 'Destek/DestekGuncelle.html', {'claim_form': claim_form, })

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





@login_required
def menu(request):
    perm = general_methods.control_access(request)


    if not perm:
        logout(request)
        return redirect('accounts:login')
    admin=MenuAdmin.objects.all()
    for m in admin:
        item=MenuDirectory(
            name=m.name,
            is_show=m.is_show,
            is_parent=m.is_parent
        )
        item.url=m.url if m.url else None
        item.fa_icon=m.fa_icon if m.fa_icon else None
        # item.parent=int(MenuDirectory.objects.get(pk=m.parent.pk).pk) if m.parent  else None
        item.sorting=m.sorting if m.sorting else None
        item.save()
    return render(request, 'Destek/Desktek-ekle.html', {})



@login_required
def dokuman_delete(request,claim_pk,pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            file = File.objects.get(pk=pk)
            claim=Claim.objects.get(pk=claim_pk)
            claim.files.remove(file)
            file.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except :
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})
