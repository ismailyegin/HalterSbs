from datetime import timedelta, datetime

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from wushu.Forms.BeltForm import BeltForm
from wushu.Forms.CategoryItemForm import CategoryItemForm
from wushu.Forms.CommunicationForm import CommunicationForm
from wushu.Forms.DisabledCommunicationForm import DisabledCommunicationForm
from wushu.Forms.DisabledPersonForm import DisabledPersonForm
from wushu.Forms.DisabledUserForm import DisabledUserForm
from wushu.Forms.LicenseForm import LicenseForm
from wushu.Forms.UserForm import UserForm
from wushu.Forms.PersonForm import PersonForm
from wushu.Forms.UserSearchForm import UserSearchForm
from wushu.models import Athlete, CategoryItem, Person, Communication, License, SportClubUser, SportsClub
from wushu.models.EnumFields import EnumFields
from wushu.models.Level import Level
from wushu.services import general_methods
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.serializers import serialize
from django.core import serializers



from django.core.paginator import Paginator
from django.shortcuts import render

import  json
def deneme(request):
    perm = general_methods.control_access_klup(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    return render(request, 'sporcu/deneme.html')


@login_required
def return_athletesdeneme(request):
    login_user = request.user
    user = User.objects.get(pk=login_user.pk)

    # print("ajax istenilen yere geldi")

    # /datatablesten gelen veri kümesi datatables degiskenine alindi
    if request.method == 'GET':
        datatables = request.GET
        # print("get islemi gerceklesti")
    elif request.method == 'POST':
        datatables = request.POST
        # print("post islemi gerceklesti")


    # /Sayfanın baska bir yerden istenmesi durumunda degerlerin None dönmemesi icin degerler try boklari icerisine alindi
    try:
        draw = int(datatables.get('draw'))
        print("draw degeri =", draw)
        # Ambil start
        start = int(datatables.get('start'))
        print("start degeri =", start)
        # Ambil length (limit)
        length = int(datatables.get('length'))
        print("lenght  degeri =", length)
        # Ambil data search
        search = datatables.get('search[value]')
        print("search degeri =", search)
    except:
        draw = 1
        start = 0
        length = 10

    if length == -1:
        if user.groups.filter(name='KulupUye'):
            sc_user = SportClubUser.objects.get(user=user)
            clubsPk = []
            clubs = SportsClub.objects.filter(clubUser=sc_user)
            for club in clubs:
                clubsPk.append(club.pk)
            modeldata = Athlete.objects.filter(licenses__sportsClub__in=clubsPk).distinct()
            total = modeldata.count()

        elif user.groups.filter(name__in=['Yonetim', 'Admin']):
            modeldata = Athlete.objects.all()
            total = Athlete.objects.count()


    else:
        if search:
            modeldata = Athlete.objects.filter(
                Q(user__last_name__icontains=search) | Q(user__first_name__icontains=search) | Q(
                    user__email__icontains=search))
            total = modeldata.count();

        else:
            if user.groups.filter(name='KulupUye'):
                sc_user = SportClubUser.objects.get(user=user)
                clubsPk = []
                clubs = SportsClub.objects.filter(clubUser=sc_user)
                for club in clubs:
                    clubsPk.append(club.pk)
                modeldata = Athlete.objects.filter(licenses__sportsClub__in=clubsPk).distinct()[start:start + length]
                total=modeldata.count()

            elif user.groups.filter(name__in=['Yonetim', 'Admin']):
                modeldata = Athlete.objects.all()[start:start + length]
                total=Athlete.objects.count()




    # /Sayfalama  islemleri ile gerekli bir sekil de istenilen sayfanın gönderilmesi gerçeklesitirildi.



    say = start+1
    start = start + length
    page = start / length

    beka = []
    for item in modeldata:
        brans = '-'
        klup = '-'
        kusak='-'
        if item.licenses.count()>0:
            if item.licenses.last().sportsClub.name is not None :
                klup = item.licenses.last().sportsClub.name

            if item.licenses.last().branch is not None:
                brans = item.licenses.last().branch
        if item.belts.count()>0:
            kusak = item.belts.last()
            kusak=kusak.definition.name
        data = {
            'say': say,
            'pk': item.pk,
            'name': item.user.first_name + item.user.last_name,
            'user': item.person.birthDate,
            'klup': klup,
            'brans':brans,
            'kusak':kusak,

        }
        beka.append(data)
        say += 1
    # print('hata geliyorum demez')

    # print(json.dumps(beka))


    # veri = [item.to_dict_json(say)  for item in modeldata ]
    # veri=serializers.serialize('json',modeldata)
    # print('veri=',veri)

    # paginator = Paginator(beka, length)
    # print("paginator=", paginator)
    # veri = paginator.page(page).object_list
    # # veri=modeldata.
    #
    # print('veri2=',veri)
    # print('veri3)',serializers.serialize('json',modeldata))

    #
    # print(total)
    # Veri istenildigi gibi paketlendi ve gönderildi
    response = {

        'data': beka,
        'draw': draw,
        'recordsTotal': total,
        'recordsFiltered': total,

    }
    return JsonResponse(response)




