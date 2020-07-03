# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-08-13 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'music_admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_id', models.CharField(blank=True, max_length=255, null=True)),
                ('music_name', models.CharField(blank=True, max_length=255, null=True)),
                ('music_img', models.CharField(blank=True, max_length=255, null=True)),
                ('music_author', models.CharField(blank=True, max_length=255, null=True)),
                ('music_album', models.CharField(blank=True, max_length=255, null=True)),
                ('isfree', models.IntegerField()),
            ],
            options={
                'db_table': 'music_music',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Musiclanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'music_musiclanguage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Musicstyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'music_musicstyle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mv_id', models.CharField(max_length=100)),
                ('mv_name', models.CharField(max_length=500)),
                ('mv_author', models.CharField(max_length=100)),
                ('mv_desc', models.CharField(max_length=800)),
                ('mv_pic', models.CharField(max_length=500)),
                ('playcount', models.CharField(db_column='playCount', max_length=100)),
                ('publishtime', models.CharField(db_column='publishTime', max_length=100)),
                ('mv_url_240', models.CharField(blank=True, max_length=800, null=True)),
                ('mv_url_480', models.CharField(blank=True, max_length=800, null=True)),
                ('mv_url_720', models.CharField(blank=True, max_length=800, null=True)),
                ('mv_url_1080', models.CharField(blank=True, max_length=800, null=True)),
                ('isfree', models.IntegerField()),
            ],
            options={
                'db_table': 'music_mv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Songlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.CharField(max_length=100)),
                ('list_title', models.CharField(max_length=500)),
                ('list_img', models.CharField(max_length=500)),
                ('list_tag', models.CharField(max_length=500)),
                ('isfree', models.IntegerField()),
            ],
            options={
                'db_table': 'music_songlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
                ('reg_time', models.DateField(null=True)),
                ('guanzhu', models.IntegerField(default=0, max_length=255)),
                ('fensi', models.IntegerField(default=0, max_length=255)),
                ('address', models.CharField(default='北京', max_length=255)),
                ('phone', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'music_user',
                'managed': False,
            },
        ),
    ]
