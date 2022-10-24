# Generated by Django 4.1.1 on 2022-10-09 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='city',
            field=models.CharField(default='Not_Available', max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='home_type',
            field=models.CharField(choices=[('House', 'House'), ('Condo', 'Condo'), ('Townhouse', 'Townhouse')], default='House', max_length=50),
        ),
        migrations.AddField(
            model_name='listing',
            name='sale_type',
            field=models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent')], default='For Sale', max_length=50),
        ),
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(default='Not_Available', max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(default='Not_Available', max_length=15),
        ),
    ]
