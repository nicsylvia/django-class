# Generated by Django 3.1.1 on 2021-12-10 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_app', '0002_auto_20211208_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactagent',
            name='phone',
            field=models.CharField(default='09061180473', max_length=12),
            preserve_default=False,
        ),
    ]
