# Generated by Django 2.2.11 on 2020-04-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('office', models.CharField(max_length=50)),
                ('establishment', models.IntegerField()),
                ('capitalStock', models.IntegerField()),
                ('sales', models.IntegerField()),
                ('employees', models.IntegerField()),
                ('averageAge', models.IntegerField()),
                ('startingSales', models.IntegerField()),
                ('workingHours', models.IntegerField()),
            ],
        ),
    ]
