# Generated by Django 5.0.7 on 2024-07-29 07:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Appeal", "0002_alter_appeal_form_agent_listened"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Appeal_Form",
            new_name="Audit",
        ),
    ]
