# Generated by Django 2.1.7 on 2021-03-30 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViolenciasCount',
            fields=[
                ('id_contador', models.AutoField(primary_key=True,
                                                 serialize=False)),
                ('ds_categoria', models.TextField()),
                ('vitimas_categoria_counter', models.IntegerField(default=0)),
            ],
        ),
    ]
