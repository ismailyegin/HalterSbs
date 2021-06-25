from builtins import print
from itertools import combinations, product
from statistics import mode

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
from sbs.models import SportClubUser, SportsClub, Competition, Athlete, CompAthlete, Weight, CompCategory, Coach, City
from sbs.models.SimpleCategory import SimpleCategory
from sbs.models.EnumFields import EnumFields
from sbs.models.SandaAthlete import SandaAthlete
from sbs.models.TaoluAthlete import TaoluAthlete
from sbs.services import general_methods
from sbs.Forms.SimplecategoryForm import SimplecategoryForm

from datetime import date,datetime
from django.utils import timezone


@login_required
def categori_ekle(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    simplecategoryForm = SimplecategoryForm()
    categoryitem = SimpleCategory.objects.all()
    if request.method == 'POST':
        simplecategoryForm = SimplecategoryForm(request.POST)
        if simplecategoryForm.is_valid():
            simplecategoryForm.save()
            messages.success(request, 'Kategori Başarıyla Güncellenmiştir.')
        else:
            messages.warning(request, 'Birşeyler ters gitti yeniden deneyiniz.')

    return render(request, 'musabaka/müsabaka-Simplecategori.html',
                  {'category_item_form': simplecategoryForm, 'categoryitem': categoryitem})


@login_required
def aplication(request, pk):
    perm = general_methods.control_access_klup(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')


    musabaka = Competition.objects.get(pk=pk)

    login_user = request.user
    user = User.objects.get(pk=login_user.pk)
    weights = Weight.objects.all()
    if user.groups.filter(name='KulupUye'):
        sc_user = SportClubUser.objects.get(user=user)
        if sc_user.dataAccessControl == True:
            if user.groups.filter(name='KulupUye'):
                clubsPk = []
                clubs = SportsClub.objects.filter(clubUser=sc_user)
                for club in clubs:
                    clubsPk.append(club.pk)

                comAthlete = CompAthlete.objects.filter(competition=pk,
                                                        athlete__licenses__sportsClub__in=clubsPk).distinct()


        else:
            messages.warning(request, 'Lütfen Eksik olan Sporcu Bilgilerini tamamlayiniz.')
            return redirect('sbs:musabakalar')
    elif user.groups.filter(name__in=['Yonetim', 'Admin']):
        comAthlete = CompAthlete.objects.filter(competition=pk).distinct()

    elif user.groups.filter(name='Antrenor'):
        coach = Coach.objects.get(user=user)
        comAthlete = CompAthlete.objects.filter(competition=pk, athlete__licenses__coach=coach).distinct()
    city=City.objects.none()
    if musabaka.compType==Competition.PERSONAL:
        city=City.objects.all()
    return render(request, 'musabaka/basvuru.html',
                  {'athletes': comAthlete, 'competition': musabaka, 'weights': weights,'city':city})




@login_required
def return_competition(request):

    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    competitions = Competition.objects.filter(startDate__year=timezone.now().year)
    year=timezone.now().year
    year=Competition.objects.values('year').distinct().order_by('year')
    return render(request, 'musabaka/sonuclar.html',{'competitions': competitions,'year':year})


@login_required
def return_competitions(request):
    perm = general_methods.control_access_klup(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    comquery=CompetitionSearchForm()
    competition = Competition.objects.filter(registerStartDate__lte=timezone.now(),
                                             registerFinishDate__gte=timezone.now())
    competitions = Competition.objects.none()


    if request.method == 'POST':
        name= request.POST.get('name')
        startDate= request.POST.get('startDate')
        compType= request.POST.get('compType')
        compGeneralType= request.POST.get('compGeneralType')
        if name or startDate or compType or compGeneralType:
            query = Q()
            if name:
                query &= Q(name__icontains=name)
            if startDate:
                query &= Q(year=int(startDate))
            if compType:
                query &= Q(compType__in=compType)
            if compGeneralType:
                query &= Q(compGeneralType__in=compGeneralType)
            competitions=Competition.objects.filter(query).order_by('-startDate').distinct()
        else:
            competitions = Competition.objects.all().order_by('-startDate')
    return render(request, 'musabaka/musabakalar.html',
                  {'competitions': competitions, 'query': comquery, 'application': competition})


@login_required
def musabaka_ekle(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    competition_form = CompetitionForm()
    if request.method == 'POST':
        competition_form = CompetitionForm(request.POST)
        if competition_form.is_valid():
            musabaka=competition_form.save(commit=False)
            musabaka.juryCount=0;
            musabaka.save()

            log = str(request.POST.get('name')) + "  Musabaka eklendi "
            log = general_methods.logwrite(request, request.user, log)

            messages.success(request, 'Müsabaka Başarıyla Kaydedilmiştir.')

            return redirect('sbs:musabaka-duzenle', pk=musabaka.pk)
        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'musabaka/musabaka-ekle.html',
                  {'competition_form': competition_form})


@login_required
def musabaka_duzenle(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    musabaka = Competition.objects.get(pk=pk)
    athletes = CompAthlete.objects.filter(competition=pk)


    weights = Weight.objects.all()
    competition_form = CompetitionForm(request.POST or None, instance=musabaka)
    if request.method == 'POST':
        if competition_form.is_valid():
            competition_form.save()
            messages.success(request, 'Müsabaka Başarıyla Güncellenmiştir.')

            log = str(request.POST.get('name')) + "  Musabaka guncellendi "
            log = general_methods.logwrite(request, request.user, log)



            return redirect('sbs:musabaka-duzenle', pk=pk)
        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'musabaka/musabaka-duzenle.html',
                  {'competition_form': competition_form, 'competition': musabaka, 'athletes': athletes,'weights':weights})


@login_required
def musabaka_sil(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Competition.objects.get(pk=pk)

            log = str(obj.name) + "  Musabaka silindi "
            log = general_methods.logwrite(request, request.user, log)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except Competition.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


def musabaka_sporcu_ekle(request, athlete_pk, competition_pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    if request.method == 'POST':
        compAthlete = CompAthlete()
        compAthlete.athlete = Athlete.objects.get(pk=athlete_pk)
        compAthlete.competition = Competition.objects.get(pk=competition_pk)
        compAthlete.sıklet = Weight.objects.get(pk=request.POST.get('weight'))
        compAthlete.total = request.POST.get('total')
        compAthlete.save()
        messages.success(request, 'Sporcu Eklenmiştir')

    return redirect('sbs:lisans-listesi')


@login_required
def musabaka_sporcu_sec(request, pk):
    perm = general_methods.control_access_klup(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    weights = Weight.objects.all()

    competition=Competition.objects.none()
    city = City.objects.none();
    if Competition.objects.filter(pk=pk):
        competition=Competition.objects.get(pk=pk)
    if competition.compType==Competition.PERSONAL:

        city=City.objects.all()

    pre_competition = Competition.objects.filter(registerStartDate__lte=timezone.now(),
                                             registerFinishDate__gte=timezone.now())

    # login_user = request.user
    # user = User.objects.get(pk=login_user.pk)
    # competition = Competition.objects.get(pk=pk)
    # weights = Weight.objects.all()
    # if user.groups.filter(name='KulupUye'):
    #     sc_user = SportClubUser.objects.get(user=user)
    #     clubsPk = []
    #     clubs = SportsClub.objects.filter(clubUser=sc_user)
    #     for club in clubs:
    #         clubsPk.append(club.pk)
    #     athletes = Athlete.objects.filter(licenses__sportsClub__in=clubsPk).distinct()
    # elif user.groups.filter(name__in=['Yonetim', 'Admin']):
    #     athletes = Athlete.objects.all()
    return render(request, 'musabaka/musabaka-sporcu-sec.html',
                  {'competition': competition, 'city':city,'weights': weights, 'pre_competition': pre_competition})
                  # ,{'athletes': athletes, 'competition': competition, })


@login_required
def return_sporcu_ajax(request):
    # print('ben geldim')
    login_user = request.user
    user = User.objects.get(pk=login_user.pk)
    # /datatablesten gelen veri kümesi datatables degiskenine alindi
    if request.method == 'GET':
        datatables = request.GET
        print(request.GET)
        secilenler = request.GET.getlist('secilenler[]')
        pk = request.GET.get('athlete')
        athlete = Athlete.objects.get(pk=pk)



        # print('pk beklenen deger =',pk)
        # kategori = CompetitionCategori.objects.get(pk=request.GET.get('cmd'))

    elif request.method == 'POST':
        datatables = request.POST


    # /Sayfanın baska bir yerden istenmesi durumunda degerlerin None dönmemesi icin degerler try boklari icerisine alindi

    try:
        draw = int(datatables.get('draw'))
        # print("draw degeri =", draw)
        # Ambil start
        start = int(datatables.get('start'))
        # print("start degeri =", start)
        # Ambil length (limit)
        length = int(datatables.get('length'))
        # print("lenght  degeri =", length)
        # Ambil data search
        search = datatables.get('search[value]')
        # print("search degeri =", search)
    except:
        draw = 1
        start = 0
        length = 10
    modeldata = Athlete.objects.none()
    if length == -1:

        # athletes = []
        # for comp in compAthlete:
        #     if comp.athlete:
        #         athletes.append(comp.athlete.pk)
        modeldata = Athlete.objects.exclude(pk=athlete.pk)
        total = Athlete.objects.exclude(pk=athlete.pk).count()







    else:
        if search:
            modeldata = Athlete.objects.none()

            athletes = []
            modeldata = Athlete.objects.filter(
                Q(user__last_name__icontains=search) | Q(user__first_name__icontains=search) | Q(
                    user__email__icontains=search)).exclude(pk=athlete.pk)

            total = modeldata.count()


        else:
            modeldata = Athlete.objects.exclude(pk=athlete.pk)[start:start + length]
            total = Athlete.objects.exclude(pk=athlete.pk).distinct().count()

    say = start + 1
    start = start + length
    page = start / length

    beka = []

    for item in modeldata:
        klup = ''
        try:
            if item.licenses:
                for lisans in item.licenses.all():
                    if lisans.sportsClub:
                        klup = str(lisans.sportsClub) + "<br>" + klup
        except:
            klup = ''
        if item.person.birthDate is not None:
            date = item.person.birthDate.strftime('%d/%m/%Y')
        else:
            date = ''
        data = {
            'id': 'row-' + str(item.pk),
            'say': say,
            'pk': item.pk,
            'tc': item.person.tc,
            'mail': item.user.email,
            'anne': item.person.motherName,
            'baba': item.person.fatherName,


            'name': item.user.first_name + ' ' + item.user.last_name,

            'birthDate': date,

            'klup': klup,

        }
        beka.append(data)
        say += 1

    response = {

        'data': beka,
        'draw': draw,
        'recordsTotal': total,
        'recordsFiltered': total,

    }
    return JsonResponse(response)





@login_required
def return_sporcu(request):
    # print('ben geldim')
    login_user = request.user
    user = User.objects.get(pk=login_user.pk)
    # /datatablesten gelen veri kümesi datatables degiskenine alindi
    if request.method == 'GET':
        datatables = request.GET
        pk = request.GET.get('cmd')
        # print('pk beklenen deger =',pk)
        competition = Competition.objects.get(pk=pk)
        # kategori = CompetitionCategori.objects.get(pk=request.GET.get('cmd'))

    elif request.method == 'POST':
        datatables = request.POST
        # print(datatables)
        # print("post islemi gerceklesti")

    # /Sayfanın baska bir yerden istenmesi durumunda degerlerin None dönmemesi icin degerler try boklari icerisine alindi
    try:
        draw = int(datatables.get('draw'))
        # print("draw degeri =", draw)
        # Ambil start
        start = int(datatables.get('start'))
        # print("start degeri =", start)
        # Ambil length (limit)
        length = int(datatables.get('length'))
        # print("lenght  degeri =", length)
        # Ambil data search
        search = datatables.get('search[value]')
        # print("search degeri =", search)
    except:
        draw = 1
        start = 0
        length = 10

    if length == -1:

        athletes = []
        for comp in compAthlete:
            if comp.athlete:
                athletes.append(comp.athlete.pk)


        if user.groups.filter(name='KulupUye'):
            sc_user = SportClubUser.objects.get(user=user)
            clubsPk = []
            clubs = SportsClub.objects.filter(clubUser=sc_user)
            for club in clubs:
                clubsPk.append(club.pk)


            modeldata = Athlete.objects.exclude(pk__in=athletes).filter(licenses__sportsClub__in=clubsPk).distinct()
            total = modeldata.count()

        elif user.groups.filter(name__in=['Yonetim', 'Admin']):
            modeldata = Athlete.objects.exclude(pk__in=athletes)
            total = Athlete.objects.exclude(pk__in=athletes).count()

        elif user.groups.filter(name='Antrenor'):
            modeldata = Athlete.objects.filter(licenses__coach__user=user).exclude(pk__in=athletes).distinct()[
                        start:start + length]

            total = Athlete.objects.filter(licenses__coach__user=user).exclude(pk__in=athletes).distinct().count()




    else:
        if search:
            modeldate=Athlete.objects.none()

            compAthlete = CompAthlete.objects.filter(competition=competition)
            athletes = []
            modeldata =Athlete.objects.filter(
                Q(user__last_name__icontains=search) | Q(user__first_name__icontains=search) | Q(
                    user__email__icontains=search))


            for comp in compAthlete:
                if comp.athlete:
                    athletes.append(comp.athlete.pk)
            if user.groups.filter(name='KulupUye'):
                sc_user = SportClubUser.objects.get(user=user)
                clubsPk = []
                clubs = SportsClub.objects.filter(clubUser=sc_user)
                for club in clubs:
                    clubsPk.append(club.pk)
                modeldata = modeldata.exclude(pk__in=athletes).filter(
                    licenses__sportsClub__in=clubsPk).distinct()
                total = modeldata.exclude(pk__in=athletes).filter(
                    licenses__sportsClub__in=clubsPk).distinct().count()
            elif user.groups.filter(name__in=['Yonetim', 'Admin']):
                modeldata = modeldata.exclude(pk__in=athletes)


            elif user.groups.filter(name='Antrenor'):
                modeldata = modeldata.filter(licenses__coach__user=user).exclude(pk__in=athletes).distinct()

            total=modeldata.count()


        else:
            compAthlete=CompAthlete.objects.filter(competition=competition)
            athletes = []
            for comp in compAthlete:
                if comp.athlete:
                        athletes.append(comp.athlete.pk)
                        print(comp.athlete)
            if user.groups.filter(name='KulupUye'):
                sc_user = SportClubUser.objects.get(user=user)
                clubsPk = []
                clubs = SportsClub.objects.filter(clubUser=sc_user)
                for club in clubs:
                    clubsPk.append(club.pk)
                modeldata = Athlete.objects.exclude(pk__in=athletes).filter(licenses__sportsClub__in=clubsPk).distinct()[start:start + length]
                total = Athlete.objects.exclude(pk__in=athletes).filter(
                    licenses__sportsClub__in=clubsPk).distinct().count()
            elif user.groups.filter(name__in=['Yonetim', 'Admin']):
                modeldata = Athlete.objects.exclude(pk__in=athletes)[start:start + length]
                total = Athlete.objects.exclude(pk__in=athletes).distinct().count()


            elif user.groups.filter(name='Antrenor'):
                modeldata = Athlete.objects.filter(licenses__coach__user=user).exclude(pk__in=athletes).distinct()[
                            start:start + length]

                total = Athlete.objects.filter(licenses__coach__user=user).exclude(pk__in=athletes).distinct().count()




    say = start + 1
    start = start + length
    page = start / length

    beka = []
    for item in modeldata:
        klup=''
        try:
            if item.licenses:
                for lisans in item.licenses.all():
                    if lisans.sportsClub:
                        klup = str(lisans.sportsClub) + "<br>" + klup
        except:
            klup=''
        if item.person.birthDate is not None:
            date = item.person.birthDate.strftime('%d/%m/%Y')
        else:
            date = ''
        data = {
            'say': say,
            'pk': item.pk,

            'name': item.user.first_name + ' ' + item.user.last_name,

            'birthDate': date,

            'klup':klup,

        }
        beka.append(data)
        say += 1


    response = {

        'data': beka,
        'draw': draw,
        'recordsTotal': total,
        'recordsFiltered': total,

    }
    return JsonResponse(response)


@login_required
def update_athlete(request, pk, competition):
    perm = general_methods.control_access_klup(request)
    login_user = request.user

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():

        try:
            user = User.objects.get(pk=login_user.pk)
            compAthlete = CompAthlete.objects.get(pk=competition)
            total = request.POST.get('total')
            siklet = request.POST.get('weight')
            silk=request.POST.get('silk')
            kop=request.POST.get('kop')
            if total is not None:
                compAthlete.total = total
            if siklet is not None:
                compAthlete.sıklet = Weight.objects.get(pk=siklet)
            if silk is not None:
                compAthlete.silk1 = silk
            if kop is not None:
                compAthlete.kop1 = kop
            if request.POST.get('city'):
                if City.objects.filter(pk=request.POST.get('city')):
                    compAthlete.city=City.objects.get(pk=request.POST.get('city'))
            compAthlete.save()

            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except SandaAthlete.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})



@login_required
def choose_athlete_update(request, pk, competition):

    perm = general_methods.control_access_klup(request)
    login_user = request.user

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        if (request.POST.get('kop') and request.POST.get('silk') and request.POST.get('weight') and request.POST.get(
                'total')):
            user = User.objects.get(pk=login_user.pk)
            competition = Competition.objects.get(pk=competition)
            compAthlete = CompAthlete.objects.get(pk=pk)
            compAthlete.competition = competition
            compAthlete.total = request.POST.get('total')
            compAthlete.sıklet = Weight.objects.get(weight=request.POST.get('weight'))
            compAthlete.silk1 = request.POST.get('silk')
            compAthlete.kop1 = request.POST.get('kop')
            if (int(request.POST.get('silk')) + int(request.POST.get('kop'))) - 20 <= int(
                    request.POST.get('total')):
                compAthlete.save()

                log = str(user.get_full_name()) + " müsabaka basvuru bilgileri güncellendi "
                log = general_methods.logwrite(request, request.user, log)


                return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
            else:
                return JsonResponse({'status': 'Fail', 'msg': 'Kural20'})
        else:
            return JsonResponse({'status': 'Fail', 'msg': 'Eksik'})

        try:
            print('')



            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except SandaAthlete.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})




@login_required
def choose_athlete(request, pk, competition):
    perm = general_methods.control_access_klup(request)
    login_user = request.user

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        print("---------------------")
        print(request.POST.get('city'))


        try:


            if (request.POST.get('total') and request.POST.get('silk') and request.POST.get('kop') and request.POST.get('weight')):

                user = User.objects.get(pk=login_user.pk)
                competition = Competition.objects.get(pk=competition)
                athlete = Athlete.objects.get(pk=pk)
                compAthlete = CompAthlete()
                compAthlete.athlete = athlete
                compAthlete.competition = competition
                compAthlete.total = request.POST.get('total')
                compAthlete.sıklet = Weight.objects.get(pk=request.POST.get('weight'))
                compAthlete.silk1 = request.POST.get('silk')
                compAthlete.kop1 = request.POST.get('kop')

                if request.POST.get('city'):
                    print('deger geldi')
                    if City.objects.filter(pk=request.POST.get('city')):
                        compAthlete.city=City.objects.get(pk=request.POST.get('city'))

                if (int(request.POST.get('silk')) + int(request.POST.get('kop'))) - 20 <= int(
                        request.POST.get('total')):
                    compAthlete.save()
                    log = str(athlete.user.get_full_name()) + "  Musabaka sporcu eklendi "
                    log = general_methods.logwrite(request, request.user, log)





                    return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
                else:
                    return JsonResponse({'status': 'Fail', 'msg': 'Kural20'})
            else:
                return JsonResponse({'status': 'Fail', 'msg': 'Eksik'})


        except SandaAthlete.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})











@login_required
def musabaka_sporcu_tamamla(request, athletes):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST':
        athletes1 = request.POST.getlist('selected_options')
        if athletes1:
            return redirect('sbs:musabaka-sporcu-tamamla', athletes=athletes1)
            # for x in athletes1:
            #
            #         athlete = Athlete.objects.get(pk=x)
            #         compAthlete = CompAthlete()
            #         compAthlete.athlete = athlete
            #         compAthlete.competition = competition
            #         compAthlete.save()
        else:
            messages.warning(request, 'Sporcu Seçiniz')

    return render(request, 'musabaka/musabaka-sonuclar.html', {'athletes': athletes})


@login_required
def musabaka_sporcu_sil(request, pk):
    perm = general_methods.control_access_klup(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            athlete = CompAthlete.objects.get(pk=pk)

            log = str(athlete.athlete.user.get_full_name()) + "  müsabakadan silindi "
            log = general_methods.logwrite(request, request.user, log)



            athlete.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except SandaAthlete.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})



@login_required
def result_list(request, pk):
    perm = general_methods.control_access_klup(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    competition = Competition.objects.get(pk=pk)

    compAthlete = CompAthlete.objects.filter(competition=pk).order_by('degree')

    for item in compAthlete:
        print(item.athlete)

    # compCategory = CompCategory.objects.filter(competition=pk).order_by('-name')

    return render(request, 'musabaka/musabaka-sonuclar.html',
                  {'compAthlete': compAthlete, 'competition': competition})



@login_required
def return_competition_ajax(request):
    # print('ben geldim')
    login_user = request.user
    user = User.objects.get(pk=login_user.pk)
    # /datatablesten gelen veri kümesi datatables degiskenine alindi
    if request.method == 'GET':
        datatables = request.GET
        pk = request.GET.get('cmd').strip()

    elif request.method == 'POST':
        datatables = request.POST
        # print(datatables)
        # print("post islemi gerceklesti")

    # /Sayfanın baska bir yerden istenmesi durumunda degerlerin None dönmemesi icin degerler try boklari icerisine alindi
    try:
        draw = int(datatables.get('draw'))
        # print("draw degeri =", draw)
        # Ambil start
        start = int(datatables.get('start'))
        # print("start degeri =", start)
        # Ambil length (limit)
        length = int(datatables.get('length'))
        # print("lenght  degeri =", length)
        # Ambil data search
        search = datatables.get('search[value]')
        # print("search degeri =", search)
    except:
        draw = 1
        start = 0
        length = 10
    modeldata=Competition.objects.none()
    if length == -1:
        print()

        # if user.groups.filter(name='KulupUye'):
        #     sc_user = SportClubUser.objects.get(user=user)
        #     clubsPk = []
        #     clubs = SportsClub.objects.filter(clubUser=sc_user)
        #     for club in clubs:
        #         clubsPk.append(club.pk)
        #
        #     modeldata = Athlete.objects.filter(licenses__sportsClub__in=clubsPk).distinct()
        #     total = modeldata.count()
        #
        # elif user.groups.filter(name__in=['Yonetim', 'Admin']):
        #     modeldata = Athlete.objects.all()
        #     total = Athlete.objects.all().count()


    else:
        if search:
            modeldata =Competition.objects.filter(
                Q(name=search))
            total = modeldata.count();

        else:
            # compAthlete=CompAthlete.objects.filter(competition=competition)
            # athletes = []
            # for comp in compAthlete:
            #     if comp.athlete:
            #             athletes.append(comp.athlete.pk)
            if user.groups.filter(name='KulupUye'):
                print('klüp üye ')
                # sc_user = SportClubUser.objects.get(user=user)
                # clubsPk = []
                # clubs = SportsClub.objects.filter(clubUser=sc_user)
                # for club in clubs:
                #     clubsPk.append(club.pk)
                # modeldata = Athlete.objects.exclude(pk__in=athletes).filter(licenses__sportsClub__in=clubsPk).distinct()[start:start + length]
                # total = mAthlete.objects.exclude(pk__in=athletes).filter(licenses__sportsClub__in=clubsPk).distinct().count()
            elif user.groups.filter(name__in=['Yonetim', 'Admin']):

                modeldata = Competition.objects.filter(year=pk)
                total =modeldata.count()


    say = start + 1
    start = start + length
    page = start / length

    beka = []
    for item in modeldata:
        data = {
            'say': say,
            'pk': item.pk,
            'name': item.name,

        }
        beka.append(data)
        say += 1

    response = {

        'data': beka,
        'draw': draw,
        'recordsTotal': total,
        'recordsFiltered': total,

    }
    return JsonResponse(response)
