from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from myapp import models
from . import forms
from .forms import ProForm


class HomeView(TemplateView):
    template_name = "index.html"


class ProView(TemplateView):
    template_name = "galerie.html"


class AboutView(TemplateView):
    template_name = "apropos.html"


class ChoixView(TemplateView):
    template_name = "choix.html"


def pro_signup_view(request):
    userForm = forms.ProUserForm()
    proForm = forms.ProForm()
    mydict = {'userForm': userForm, 'proForm': proForm}
    if request.method == 'POST':
        userForm = forms.ProUserForm(request.POST)
        proForm = forms.ProForm(request.POST, request.FILES)
        if userForm.is_valid() and proForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            pro = proForm.save(commit=False)
            pro.user = user
            pro = pro.save()
            my_pro_group = Group.objects.get_or_create(name='PRO')
            my_pro_group[0].user_set.add(user)
        return HttpResponseRedirect('prologin')
    return render(request, 'ipro.html', context=mydict)


def clt_signup_view(request):
    userForm = forms.CltUserForm()
    cltForm = forms.CltForm()
    mydict = {'userForm': userForm, 'cltForm': cltForm}
    if request.method == 'POST':
        userForm = forms.CltUserForm(request.POST)
        cltForm = forms.CltForm(request.POST, request.FILES)
        if userForm.is_valid() and cltForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            clt = cltForm.save(commit=False)
            clt.user = user
            clt.proAssignedId = request.POST.get('proAssignedId')
            clt = clt.save()
            my_clt_group = Group.objects.get_or_create(name='CLT')
            my_clt_group[0].user_set.add(user)
        return HttpResponseRedirect('cltlogin')
    return render(request, 'iclt.html', context=mydict)


class Proclick(TemplateView):
    template_name = "proclick.html"


class Cltclick(TemplateView):
    template_name = "cltclick.html"


# -----------for checking user is doctor , patient or admin(by sumit)
def is_pro(user):
    return user.groups.filter(name='PRO').exists()


def is_clt(user):
    return user.groups.filter(name='CLT').exists()
# def signup(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#         return HttpResponse("Merci de vous êtes inscrit")
#     else:
#         form = SignupForm()
#     return render(request, "accounts/signup.html", {"form": form})


# def prosignup(request):
#     if request.method == "POST":
#         form = ProForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect(request.path)
#     else:
#         form = ProForm()
#     return render(request, "accounts/prosignup.html", {"form": form})

#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,DOCTOR OR PATIENT
def afterlogin_view(request):
        return redirect('admin-dashboard')
    # elif is_doctor(request.user):
    #     accountapproval = models.Doctor.objects.all().filter(user_id=request.user.id, status=True)
    #     if accountapproval:
    #         return redirect('doctor-dashboard')
    #     else:
    #         return render(request, 'hospital/doctor_wait_for_approval.html')
    # elif is_patient(request.user):
    #     accountapproval = models.Patient.objects.all().filter(user_id=request.user.id, status=True)
    #     if accountapproval:
    #         return redirect('patient-dashboard')
    #     else:
    #         return render(request, 'hospital/patient_wait_for_approval.html')
# ---------------------------------------------------------------------------------
# ------------------------ DOCTOR RELATED VIEWS START ------------------------------
# ---------------------------------------------------------------------------------
@login_required(login_url='prologin')
@user_passes_test(is_pro)
def pro_dashboard_view(request):
    # for three cards
    cltcount = models.Clt.objects.all().filter(status=True, proAssignId=request.user.id).count()
    rdvcount = models.Rdv.objects.all().filter(status=True, proId=request.user.id).count()
    cltdischarged = models.CltDischargeDetails.objects.all().distinct().filter(
        ProAssignedName=request.user.first_name).count()

    # for  table in doctor dashboard
    rdv = models.Rdv.objects.all().filter(status=True, proId=request.user.id).order_by('-id')
    cltid = []
    for a in rdv:
        cltid.append(a.patientId)
    clts = models.Clt.objects.all().filter(status=True, user_id__in=cltid).order_by('-id')
    rdvs = zip(rdv, clts)
    mydict = {
        'cltcount': cltcount,
        'rdvcount': rdvcount,
        'cltdischarged': cltdischarged,
        'rdvs': rdvs,
        'pro': models.Pro.objects.get(user_id=request.user.id),  # for profile picture of doctor in sidebar
    }
    return render(request, 'pro_dashboard.html', context=mydict)


# ---------------------------------------------------------------------------------
# ------------------------ PATIENT RELATED VIEWS START ------------------------------
# ---------------------------------------------------------------------------------
@login_required(login_url='patientlogin')
@user_passes_test(is_clt)
def clt_dashboard_view(request):
    clt = models.Clt.objects.get(user_id=request.user.id)
    pro = models.Pro.objects.get(user_id=clt.proAssignId)
    mydict = {
        'clt': clt,
        'proName': pro.get_name,
        'proMobile': pro.contact,
        'proAddress': pro.email,
        'symptoms': clt.symptoms,
        'proSpecialisation': pro.spec,
        'admitDate': clt.admitDate,
    }
    return render(request, 'clt_dashboard.html', context=mydict)
