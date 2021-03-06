# Generated by Django 3.2.9 on 2021-12-01 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parts_demand_api', '0002_auto_20211201_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartsDemand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_description', models.CharField(max_length=100, verbose_name='Descrição da peça')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('phone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('status', models.BooleanField(default=True)),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parts_demand_api.deliveryaddress')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
