# Generated by Django 3.0.4 on 2020-04-09 13:17

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '标签分类',
                'verbose_name_plural': '标签分类',
                'db_table': 'ty_Music_Type',
            },
        ),
        migrations.CreateModel(
            name='SingerName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='歌手姓名')),
                ('gender', models.CharField(max_length=8, verbose_name='歌手性别')),
            ],
            options={
                'verbose_name': '歌手姓名',
                'verbose_name_plural': '歌手姓名',
                'db_table': 'ty_SingerName',
            },
        ),
        migrations.CreateModel(
            name='SingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_URL', models.CharField(max_length=255, verbose_name='头像')),
                ('singer_info', mdeditor.fields.MDTextField(verbose_name='歌手简介')),
                ('singer_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sing.SingerName', verbose_name='歌手姓名')),
                ('singer_type', models.ManyToManyField(to='sing.Flag', verbose_name='歌手标签')),
            ],
            options={
                'verbose_name': '歌手信息',
                'verbose_name_plural': '歌手信息',
                'db_table': 'ty_Sing_Info',
            },
        ),
        migrations.CreateModel(
            name='Zhuangji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='专辑名称')),
                ('image_URL', models.CharField(max_length=255, verbose_name='专辑配图链接')),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sing.SingInfo', verbose_name='专辑作者')),
            ],
            options={
                'verbose_name': '专辑信息',
                'verbose_name_plural': '专辑信息',
                'db_table': 'ty_Zhuangji',
            },
        ),
    ]
