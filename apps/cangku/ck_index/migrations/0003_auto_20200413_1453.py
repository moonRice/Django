# Generated by Django 3.0.4 on 2020-04-13 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ck_yuangong', '0001_initial'),
        ('ck_index', '0002_gonggao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gonggao',
            name='auth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ck_yuangong.yuangong', verbose_name='发布人'),
        ),
    ]
