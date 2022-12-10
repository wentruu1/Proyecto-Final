# Generated by Django 4.1.3 on 2022-11-16 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_correspondencia_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='estado',
            field=models.CharField(choices=[('No', 'No Recibido'), ('Si', 'Recibido')], default='No', max_length=15),
        ),
    ]
