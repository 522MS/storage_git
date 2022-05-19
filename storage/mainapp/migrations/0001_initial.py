# Generated by Django 4.0.4 on 2022-05-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название файла')),
                ('uploadedFile', models.FileField(null=True, upload_to='', verbose_name='Файл')),
            ],
        ),
    ]