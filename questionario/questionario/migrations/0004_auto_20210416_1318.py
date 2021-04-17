# Generated by Django 2.1.7 on 2021-04-16 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0003_contatoviolencia_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaContato',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nome_categoria', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='contatoviolencia',
            name='categoria',
        ),
        migrations.AddField(
            model_name='contatoviolencia',
            name='categoria_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='questionario.CategoriaContato'),
            preserve_default=False,
        ),
    ]