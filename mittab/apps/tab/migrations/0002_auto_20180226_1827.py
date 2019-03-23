# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-26 18:27


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='hybrid_school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hybrid_school', to='tab.School'),
        ),
        migrations.AlterField(
            model_name='round',
            name='judges',
            field=models.ManyToManyField(blank=True, related_name='judges', to='tab.Judge'),
        ),
    ]
