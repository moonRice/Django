# Generated by Django 3.0.4 on 2020-04-28 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ck_yuangong', '0001_initial'),
        ('ck_index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='sjr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ck_yuangong.yuangong', verbose_name='收件人'),
        ),
        migrations.AddField(
            model_name='gonggao',
            name='auth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ck_yuangong.yuangong', verbose_name='发布人'),
        ),
    ]