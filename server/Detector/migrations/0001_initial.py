# Generated by Django 3.2.17 on 2023-02-10 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Xrays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=30)),
                ('uploadedOn', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='uploadedXrays/')),
                ('confidence', models.FloatField(default=1)),
                ('result', models.CharField(max_length=30)),
                ('uploadedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
