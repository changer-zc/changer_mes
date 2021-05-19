# Generated by Django 2.1.15 on 2021-05-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ware_house',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='料号')),
                ('item_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='名称')),
                ('numbers', models.CharField(blank=True, max_length=255, null=True, verbose_name='数量')),
                ('location', models.CharField(choices=[('成品仓', '成品仓'), ('半成品仓', '半成品仓'), ('电子库房', '电子库房')], default='成品仓', max_length=255, null=True, verbose_name='库位')),
                ('supplier', models.CharField(blank=True, max_length=255, null=True, verbose_name='厂商')),
                ('inventory_time', models.DateTimeField(blank=True, null=True, verbose_name='盘点时间')),
            ],
            options={
                'db_table': 'ware_house',
                'managed': True,
            },
        ),
    ]