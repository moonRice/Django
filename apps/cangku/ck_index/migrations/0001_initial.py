# Generated by Django 3.0.4 on 2020-04-06 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='小组名称')),
            ],
            options={
                'verbose_name': '小组信息',
                'verbose_name_plural': '小组信息',
                'db_table': 'ck_groups',
            },
        ),
        migrations.CreateModel(
            name='types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='类型')),
            ],
            options={
                'verbose_name': '仓库主要信息',
                'verbose_name_plural': '仓库主要信息',
                'db_table': 'ck_types',
            },
        ),
    ]
