# Generated by Django 2.1.7 on 2021-03-30 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frases',
            fields=[
                ('id_frase', models.AutoField(primary_key=True, serialize=False)),
                ('ds_frase', models.TextField()),
            ],
        ),
    ]
