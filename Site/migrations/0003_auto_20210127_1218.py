# Generated by Django 3.1.5 on 2021-01-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0002_auto_20210127_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='descricao',
            field=models.TextField(max_length=200, verbose_name='Descrição'),
        ),
    ]
