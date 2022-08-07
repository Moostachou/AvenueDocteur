from django.contrib import admin
from .models import Pro, Clt, Rdv, CltDischargeDetails


@admin.register(Pro)
class Professionels(admin.ModelAdmin):
    pass
    list_per_page = 100


@admin.register(Clt)
class Patients(admin.ModelAdmin):
    pass
    list_per_page = 100


@admin.register(Rdv)
class RendezVous(admin.ModelAdmin):
    pass


@admin.register(CltDischargeDetails)
class DechargePatient(admin.ModelAdmin):
    pass
