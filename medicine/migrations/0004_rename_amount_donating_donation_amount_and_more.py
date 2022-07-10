# Generated by Django 4.0.2 on 2022-07-10 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_calculationunits'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donating',
            old_name='amount',
            new_name='donation_amount',
        ),
        migrations.RenameField(
            model_name='medicine',
            old_name='price',
            new_name='set_price',
        ),
        migrations.RenameField(
            model_name='purchasing',
            old_name='units',
            new_name='units_sold',
        ),
    ]