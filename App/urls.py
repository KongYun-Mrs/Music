#   !/usr/bin/env python3
#   -*- coding: utf-8 -*-
#   Created on 2019-08-08  15:31
from django.conf.urls import url

from App import views

urlpatterns = [
    # 首页
    url(r'^$', views.index, name='index'),
    # 我的音乐
    url(r'^my/$', views.my_music, name='my_music'),
    # 排行
    url(r'^ranking/$', views.ranking, name='ranking'),
    # mv
    url(r'^mv/$', views.mv, name='mv'),
    # 商城
    url(r'^store/$', views.store, name='store'),
    url(r'^store/(\d+)/$', views.store, name='store1'),
    # 音乐人
    url(r'^musician/$', views.musician, name='musician'),
    # 下载客户端
    url(r'^download/$', views.download, name='download'),
    # 搜索
    url(r'^search/$', views.search, name='download'),
    # 登陆
    url(r'^sigin/$', views.login, name='login'),
    # 注册
    url(r'^signup/$', views.register, name='register'),
    # 退出登录
    url(r'^exit/$',views.exit,name='exit'),
    # 用户设置
    url(r'^profile/$', views.settings, name='profile'),
    #验证码
    url(r'^get_verify_img/$',views.get_verify_img,name='get_verify_img'),
    # 修改用户信息
    url(r'^modify/$',views.modify_infor,name='modify_infor'),
    # 激活
    # url(r'^activate/(?P<token>.+)/$', views.activate_user, name='activate'),
    #用户反馈
    url(r'^user_response/$', views.user_response, name='user_response'),
    # 积分兑换
    url(r'^rewards_points/(\d+)/$',views.rewards_points,name='rewards_points'),
]
