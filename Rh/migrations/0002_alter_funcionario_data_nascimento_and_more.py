# Generated by Django 4.0.5 on 2022-06-30 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='data_nascimento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='departamento',
            field=models.CharField(choices=[('ES', 'Estagiário'), ('AS', 'Assistente'), ('JR', 'Júnior'), ('PL', 'Pleno'), ('SR', 'Sênior'), ('GR', 'Gerente')], max_length=2),
        ),
    ]
