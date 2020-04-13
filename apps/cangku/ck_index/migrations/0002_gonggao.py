# Generated by Django 3.0.4 on 2020-04-13 06:27

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ck_yuangong', '0001_initial'),
        ('ck_index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gonggao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='公告标题')),
                ('context', mdeditor.fields.MDTextField()),
                ('auth', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='ck_yuangong.yuangong', verbose_name='发布人')),
            ],
            options={
                'verbose_name': '公告',
                'verbose_name_plural': '公告',
                'db_table': 'ck_gonggao',
            },
        ),
    ]
