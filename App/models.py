# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
from django.db.models import ForeignKey


class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'music_admin'




class Musiclanguage(models.Model):
    language = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'music_musiclanguage'


class Musicstyle(models.Model):
    style = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'music_musicstyle'


class Mv(models.Model):
    mv_id = models.CharField(max_length=100)
    mv_name = models.CharField(max_length=500)
    mv_author = models.CharField(max_length=100)
    mv_desc = models.CharField(max_length=800)
    mv_pic = models.CharField(max_length=500)
    playcount = models.CharField(db_column='playCount', max_length=100)  # Field name made lowercase.
    publishtime = models.CharField(db_column='publishTime', max_length=100)  # Field name made lowercase.
    mv_url_240 = models.CharField(max_length=800, blank=True, null=True)
    mv_url_480 = models.CharField(max_length=800, blank=True, null=True)
    mv_url_720 = models.CharField(max_length=800, blank=True, null=True)
    mv_url_1080 = models.CharField(max_length=800, blank=True, null=True)
    isfree = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'music_mv'


class Songlist(models.Model):
    list_id = models.CharField(max_length=100)
    list_title = models.CharField(max_length=500)
    list_img = models.CharField(max_length=500)
    list_tag = models.CharField(max_length=500)
    language = models.ForeignKey(Musiclanguage, models.DO_NOTHING, blank=True, null=True)
    style = models.ForeignKey(Musicstyle, models.DO_NOTHING, blank=True, null=True)
    isfree = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'music_songlist'


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    reg_time = models.DateField(null=True)
    guanzhu=models.IntegerField(default=0)
    fensi=models.IntegerField(default=0)
    address=models.CharField(max_length=255,default='北京')
    phone=models.CharField(max_length=255)
    avatar=models.ImageField(upload_to='photo')


    class Meta:
        managed = False
        db_table = 'music_user'



class User_Response(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    suggest=models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'user_response'


class Music(models.Model):
    music_id = models.CharField(max_length=255, blank=True, null=True)
    music_name = models.CharField(max_length=255, blank=True, null=True)
    music_img = models.CharField(max_length=255, blank=True, null=True)
    music_author = models.CharField(max_length=255, blank=True, null=True)
    music_album = models.CharField(max_length=255, blank=True, null=True)
    music_list_id = models.ForeignKey('Songlist', models.DO_NOTHING, blank=True, null=True)
    score = models.IntegerField(default=0)
    isfree = models.IntegerField()
    # 多对多
    music_user1 = models.ManyToManyField(User, related_name='music',through='Orders')

    class Meta:
        managed = False
        db_table = 'music_music'




# 中间表
class Orders(models.Model):
    music=ForeignKey(Music,on_delete=models.CASCADE,db_column='mid')
    music_user=ForeignKey(User,on_delete=models.CASCADE,db_column='uid')


    class Meta:
        db_table = 'App_orders'





