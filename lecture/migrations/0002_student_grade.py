# Generated by Django 3.0.3 on 2020-02-07 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.IntegerField(default=1),
        ),
    ]
