# Generated by Django 4.1.2 on 2022-11-06 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sala',
            name='num_sala',
        ),
        migrations.AddField(
            model_name='sala',
            name='cod_sala',
            field=models.CharField(default='a', max_length=50),
        ),
    ]
