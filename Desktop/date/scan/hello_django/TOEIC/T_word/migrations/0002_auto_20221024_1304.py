# Generated by Django 3.2.15 on 2022-10-24 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('T_word', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adj_word',
            name='en_word',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='adv_word',
            name='en_word',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='in_word',
            name='en_word',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='n_word',
            name='en_word',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='other_word',
            name='en_word',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='v_word',
            name='en_word',
            field=models.CharField(max_length=200),
        ),
    ]
