# Generated by Django 4.2.7 on 2023-11-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SplitWiseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('participants', models.ManyToManyField(to='SplitWiseApp.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]