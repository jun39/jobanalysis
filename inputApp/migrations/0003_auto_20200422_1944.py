# Generated by Django 2.2.11 on 2020-04-22 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inputApp', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_name', models.CharField(default='業界名', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='industry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inputApp.Industry'),
        ),
    ]
