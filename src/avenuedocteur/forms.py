from django import forms
from django.contrib.auth.models import User

from myapp import models


# class SignupForm(forms.Form):
#     nom = forms.CharField(max_length=20)
#     prenom = forms.CharField(max_length=25)
#     email = forms.EmailField()
#     mdp = forms.CharField(min_length=6, widget=forms.PasswordInput())
#     cgu_accept = forms.BooleanField(initial=True)
#
#     def clean_nom(self):
#         nom = self.cleaned_data.get("nom")
#         if "$" in nom:
#             raise forms.ValidationError("Le nom ne peut pas contenir de symbole $")
#         return nom


class ProUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class ProForm(forms.ModelForm):
    class Meta:
        model = models.Pro
        fields = ['email', 'contact', 'spec', 'status', 'photo']


# class ProForm(forms.ModelForm):
#     class Meta:
#         model = Pro
#         fields = [
#             "spec",
#             "contact",
#             "email",
#             "photo",
#             "cabinet",
#             "status",
#             "cond",
#         ]
# labels = {"contact": "numéro de téléphone",
#          "spec": "Spécialisation",
#       }
# widgets = {"dispo": forms.SelectDateWidget(years=range(2022, 2023))}


class CltUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class CltForm(forms.ModelForm):
    # this is the extrafield for linking patient and their assigend doctor
    # this will show dropdown __str__ method doctor model is shown on html so override it
    # to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    proAssignedId = forms.ModelChoiceField(queryset=models.Pro.objects.all().filter(status=True),
                                           empty_label="Nom et Specialité", to_field_name="user_id")

    class Meta:
        model = models.Clt
        fields = ['email', 'contact', 'status', 'symptoms', 'photo']


class RdvForm(forms.ModelForm):
    proId = forms.ModelChoiceField(queryset=models.Pro.objects.all().filter(status=True),
                                   empty_label="Nom du Professionnel et Specialistaion", to_field_name="user_id")
    cltId = forms.ModelChoiceField(queryset=models.Clt.objects.all().filter(status=True),
                                   empty_label="Nom du Client et Symptômes", to_field_name="user_id")

    class Meta:
        model = models.Rdv
        fields = ['comm', 'status']


class PatientAppointmentForm(forms.ModelForm):
    proId = forms.ModelChoiceField(queryset=models.Pro.objects.all().filter(status=True),
                                   empty_label="Nom du Professionnel et Specialistaion", to_field_name="user_id")

    class Meta:
        model = models.Rdv
        fields = ['comm', 'status']
