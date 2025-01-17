# Generated by Django 4.1.7 on 2023-04-08 20:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JohnCarAirCo', '0007_alter_serviceorder_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techniciandetails',
            name='tech_sched',
        ),
        migrations.AddField(
            model_name='salesorder',
            name='delivery_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='productunit',
            name='unit_stock',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='TechnicianSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_sched_day', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('tech_sched_time_start', models.TimeField()),
                ('tech_sched_time_end', models.TimeField()),
                ('tech_sched_status', models.BooleanField(default=True)),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='JohnCarAirCo.techniciandetails')),
            ],
        ),
    ]
