# Generated by Django 3.2.7 on 2022-05-13 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_saved', models.CharField(max_length=120)),
                ('body_saved', models.TextField()),
            ],
        ),
    ]
