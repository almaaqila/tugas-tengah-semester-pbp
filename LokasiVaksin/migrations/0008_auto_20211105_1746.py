# Generated by Django 3.2.8 on 2021-11-05 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LokasiVaksin', '0007_auto_20211105_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addlokasi',
            name='provinsi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='LokasiVaksin.provinsi'),
        ),
        migrations.AlterField(
            model_name='addlokasi',
            name='pulau',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='LokasiVaksin.pulau'),
        ),
    ]