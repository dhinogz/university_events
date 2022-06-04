# Generated by Django 4.0.4 on 2022-06-04 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='major',
        ),
        migrations.AddField(
            model_name='event',
            name='majors',
            field=models.ManyToManyField(related_name='events', to='core.major', verbose_name='majors'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(related_name='events', to='core.tag', verbose_name='tags'),
        ),
    ]