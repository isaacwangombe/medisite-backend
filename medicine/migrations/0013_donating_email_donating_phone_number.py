# Generated by Django 4.0.2 on 2022-07-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0012_alter_disease_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='donating',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donating',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]