# Generated by Django 2.1.7 on 2021-05-17 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0006_remove_questionario_categoria_violencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario',
            name='arvore_decisao',
            field=models.TextField(),
        ),
    ]
