# Generated by Django 5.1.3 on 2025-06-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_department_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='served_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
