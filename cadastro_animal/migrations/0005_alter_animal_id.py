# Generated by Django 4.2.11 on 2024-03-29 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_animal', '0004_alter_animal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='id',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
    ]