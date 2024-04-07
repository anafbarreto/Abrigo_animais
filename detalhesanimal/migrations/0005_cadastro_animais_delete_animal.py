# Generated by Django 4.2.11 on 2024-04-05 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detalhesanimal', '0004_animal_delete_cadastro_animal'),
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro_animais',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('especie', models.CharField(choices=[('cachorro', 'Cachorro'), ('gato', 'Gato')], max_length=10)),
                ('raca', models.CharField(max_length=20)),
                ('porte', models.CharField(max_length=10)),
                ('sexo', models.CharField(choices=[('macho', 'Macho'), ('femea', 'Fêmea')], max_length=10)),
                ('castrado', models.BooleanField(default=False)),
                ('vacinado', models.BooleanField(default=False)),
                ('doencas_existentes', models.TextField(blank=True)),
                ('adotado', models.BooleanField(default=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cadastro de animais',
                'ordering': ['-data'],
            },
        ),
        migrations.DeleteModel(
            name='Animal',
        ),
    ]
