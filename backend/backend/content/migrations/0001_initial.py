# Generated by Django 2.1.4 on 2018-12-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to='')),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
