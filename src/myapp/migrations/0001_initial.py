# Generated by Django 4.0.4 on 2022-05-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.TextField()),
                ('contact', models.CharField(max_length=10)),
                ('specialisation', models.CharField(max_length=50)),
                ('date', models.DateField(blank=True)),
            ],
        ),
    ]