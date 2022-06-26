# Generated by Django 3.2.13 on 2022-06-26 09:05

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20220626_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default= datetime.date.today),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]