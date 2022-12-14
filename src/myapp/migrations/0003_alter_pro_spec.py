# Generated by Django 4.0.6 on 2022-07-28 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_cltdischargedetails_rdv_alter_pro_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pro',
            name='spec',
            field=models.CharField(choices=[('Generaliste', 'Generaliste'), ('Cardiologue', 'Cardiologue'), ('Dentiste', 'Dentiste'), ('Dermatologue', 'Dermatologue'), ('ORL', 'ORL'), ('Neurologue', 'Neurologue'), ('Pédiatre', 'Pédiatre'), ('Gynécologue', 'Gynécologue'), ('Psychiatre', 'Psychiatre'), ('Spécialiste en médecine durgence', 'Spécialiste en médecine durgence'), ('Allergologues/Immunologues', 'Allergologues/Immunologues'), ('Anesthésistes', 'Anesthésistes'), ('Chirurgiens du côlon et du rectum', 'Chirurgiens du côlon et du rectum')], default='Generaliste', max_length=50),
        ),
    ]
