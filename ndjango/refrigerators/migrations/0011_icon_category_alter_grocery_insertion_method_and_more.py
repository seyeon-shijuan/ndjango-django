# Generated by Django 4.1.7 on 2023-05-09 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('refrigerators', '0010_barcodeinfo_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='icon',
            name='category',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='insertion_method',
            field=models.CharField(choices=[('manual', 'Manual'), ('photo', 'Photo'), ('barcode', 'Barcode')], default='manual', max_length=50),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='userid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.JSONField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
