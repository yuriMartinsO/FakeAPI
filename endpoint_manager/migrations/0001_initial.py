# Generated by Django 4.0.5 on 2022-06-30 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseRoute', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]