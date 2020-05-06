# Generated by Django 3.0.6 on 2020-05-06 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ck_cangku', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dingdan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255, verbose_name='用户信息')),
                ('dingdanhao', models.CharField(max_length=255, verbose_name='订单号')),
                ('baoxian_id', models.IntegerField(verbose_name='订单内的商品id')),
                ('price', models.IntegerField(verbose_name='订单价格')),
                ('is_paid', models.CharField(max_length=255, verbose_name='是否已经支付')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
                'db_table': 'ck_dingdan',
            },
        ),
    ]