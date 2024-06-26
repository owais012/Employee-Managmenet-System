# Generated by Django 5.0.3 on 2024-04-07 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0004_alter_leavebalance_total_leave_days"),
    ]

    operations = [
        migrations.CreateModel(
            name="LeaveHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "leave",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myApp.leave"
                    ),
                ),
                (
                    "leave_balance",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myApp.leavebalance",
                    ),
                ),
            ],
        ),
    ]
