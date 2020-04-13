# Generated by Django 3.0.4 on 2020-04-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ck_yuangong', '0001_initial'),
        ('ck_cangku', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='yuanqu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='园区名称')),
                ('cangku', models.ManyToManyField(to='ck_cangku.cangku', verbose_name='包含的仓库')),
                ('user', models.ManyToManyField(to='ck_yuangong.yuangong', verbose_name='园区负责人')),
            ],
            options={
                'verbose_name': '园区信息',
                'verbose_name_plural': '园区信息',
                'db_table': 'ck_yuanqu',
            },
        ),
    ]
