# Generated by Django 4.2.17 on 2024-12-12 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesApp', '0004_notes_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='version',
            field=models.PositiveIntegerField(default=0),
        ),
    ]