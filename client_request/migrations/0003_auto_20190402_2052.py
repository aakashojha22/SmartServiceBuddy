# Generated by Django 2.1.3 on 2019-04-02 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_request', '0002_auto_20190402_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientrequest',
            name='service_man',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serivce_man_appointed', to='service_man.ServiceManInfo'),
        ),
    ]
