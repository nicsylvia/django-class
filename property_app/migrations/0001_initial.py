# Generated by Django 3.1.1 on 2021-12-08 19:55

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
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'LOCATION',
            },
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type_name', models.CharField(max_length=60)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True)),
                ('profile', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('designation', models.CharField(max_length=30)),
                ('Biography', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Team',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.FloatField()),
                ('offer_type', models.CharField(default='', max_length=25, verbose_name='Offer Type')),
                ('image1', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('image2', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('image3', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_app.location')),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_app.propertytype')),
            ],
            options={
                'verbose_name_plural': 'property',
            },
        ),
        migrations.CreateModel(
            name='ContactAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_app.property')),
            ],
        ),
    ]
