# Generated by Django 4.2.18 on 2025-02-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch_profile', '0003_remove_sch_profile_verified_sch_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sch_profile',
            name='status',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
