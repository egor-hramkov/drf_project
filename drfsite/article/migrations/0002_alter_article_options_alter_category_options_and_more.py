# Generated by Django 4.1.1 on 2022-09-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-time_created', 'title'], 'verbose_name': 'Статьи', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default=None, max_length=100, verbose_name='Заголовок'),
        ),
    ]
