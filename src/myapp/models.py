from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class Specialisation(models.Model):
#     nom = models.CharField(max_length=40)
#     description = models.TextField()
#
#     class Meta:
#         verbose_name = "Specialisation"
#         ordering = ["nom"]
#
#     def __str__(self):
#         return self.nom

specialisations = [('Generaliste', 'Generaliste'),
                   ('Cardiologue', 'Cardiologue'),
                   ('Dentiste', 'Dentiste'),
                   ('Dermatologue', 'Dermatologue'),
                   ('ORL', 'ORL'),
                   ('Neurologue', 'Neurologue'),
                   ('Pédiatre', 'Pédiatre'),
                   ('Gynécologue', 'Gynécologue'),
                   ('Psychiatre', 'Psychiatre'),
                   ('Spécialiste en médecine d''urgence', 'Spécialiste en médecine d''urgence'),
                   ('Allergologues/Immunologues', 'Allergologues/Immunologues'),
                   ('Anesthésistes', 'Anesthésistes'),
                   ('Chirurgiens du côlon et du rectum', 'Chirurgiens du côlon et du rectum')
                   ]


class Clt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="clt", null=True, blank=True)
    photo = models.ImageField(blank=True, null=True, upload_to='photo/patients/')
    contact = models.CharField(max_length=10)
    admitDate = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=False, null=True)
    symptoms = models.CharField(max_length=100, blank=True)
    proAssignId = models.PositiveIntegerField(null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Patient"

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name + " (" + self.symptoms + ")"


class Pro(models.Model):
    # spec = models.ForeignKey(Specialisation, on_delete=models.SET_NULL, null=True)
    spec = models.CharField(max_length=50, choices=specialisations, default='Generaliste')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Pro", null=True, blank=True)
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, blank=False, null=True)
    photo = models.ImageField(blank=True, upload_to='photo/docteurs/', null=True)
    status = models.BooleanField(default=False)
    cond = models.BooleanField(default=False, verbose_name="Conditions")

    class Meta:
        verbose_name = "Professionel"

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.spec)


class Rdv(models.Model):
    proId = models.PositiveIntegerField(null=True)
    cltId = models.PositiveIntegerField(null=True)
    proName = models.CharField(max_length=40, null=True)
    cltName = models.CharField(max_length=40, null=True)
    rdvDate = models.DateTimeField(auto_now=True)
    comm = models.TextField()
    status = models.BooleanField(default=False)


class CltDischargeDetails(models.Model):
    cltId = models.PositiveIntegerField(null=True)
    cltName = models.CharField(max_length=40)
    ProAssignedName = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    symptoms = models.CharField(max_length=100, null=True)

    admitDate = models.DateField(null=False)
    releaseDate = models.DateField(null=False)
    daySpent = models.PositiveIntegerField(null=False)

    roomCharge = models.PositiveIntegerField(null=False)
    medicineCost = models.PositiveIntegerField(null=False)
    doctorFee = models.PositiveIntegerField(null=False)
    OtherCharge = models.PositiveIntegerField(null=False)
    total = models.PositiveIntegerField(null=False)
