import datetime
import os
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from App import models
from App.RegisterForm import *
import io
from PIL import ImageDraw
from PIL import ImageFont
from django.http import HttpResponse
from PIL import Image
import random
from App.models import User_Response, Music
from CloudMusic.settings import PHOTO_STYLE, MAX_FILE_SIZE,COUNTOFPAGE, PAGERANGE


# 获取头像
def catch_photo(request):
    username=request.session.get('username')
    if username:
        user = User.objects.get(username=username)
        path = "uplod/" + str(user.avatar)
        return path
    else:
        path = '/uplod/photo/7.jpg'
        return path

# 首页
def index(request):
    path=catch_photo(request)
    username = request.session.get('username')
    if username:
        user1 = User.objects.get(username=username)
        return render(request, 'app/index.html', locals())
    return render(request, 'app/index.html',locals())


# 我的音乐
def my_music(request):
    return render(request, 'app/genres.html')   # 显示流派页面


# 排行
def ranking(request):
    return HttpResponse('ranking')


# mv
def mv(request):
    return render(request, 'app/video.html')


# 商城
def store(request,page='1'):
    # 获取头像
    path = catch_photo(request)
    page = int(page)
    # 分页
    pager=list_page(page)
    return render(request,'app/shop.html',locals())




# 分页
def list_page(page):
    music=Music.objects.filter(isfree=0).defer('music_list_id')
    # 分页
    paginator= Paginator(music, COUNTOFPAGE)
    page = int(page)
    pager = paginator.page(page)  # 指定页码
    # 自定义页码列表
    if paginator.num_pages > PAGERANGE:
        if page - 5 <= 0:
            my_page_range = range(1, 11)
        elif page + 4 > paginator.num_pages:
            my_page_range = range(paginator.num_pages - 9, paginator.num_pages + 1)
        else:
            my_page_range = range(page - 5, page + 5)
    else:  # 总页数小于我要每页显示数
        my_page_range = paginator.page_range
        # 将自定义页码列表赋给页码的列表
    pager.page_range = my_page_range
    return pager



# 音乐人
def musician(request):
    return HttpResponse('musician')


# 下载客户端
def download(request):
    return HttpResponse('download')


# 搜索
def search(request):
    return HttpResponse('search')


# 登录
def login(request):
    path = catch_photo(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 查询出登录用户的信息
        if username and password:
            user=User.objects.filter(username=username)
            if user:
                if check_password(password,user[0].password):
                    request.session['username'] = username
                    print('登陆成功')
                    # 每登录一次积分加10
                    user[0].score+=10
                    user[0].save()
                    print(user[0].score)
                    path = "uplod/" + str(user[0].avatar)
                    return render(request, 'app/index.html', locals())
            return render(request, 'app/signin.html', {'msg': '密码错误或用户未激活'})
    return render(request, 'app/signin.html', locals())


# 注册
def register(request):
    # 实例化form
    path = catch_photo(request)
    form_obj = RegForms()
    if request.method == 'POST':
        regtime = datetime.date.today()#注册日期
        password=request.POST.get('password')
        code=request.POST.get('code')
        server_code=request.session.get('code')
        if password:
            form_obj=RegForms(request.POST)
            if form_obj.is_valid():
                if code.lower()==server_code.lower():
                    username = form_obj.cleaned_data["username"]
                    password = form_obj.cleaned_data["password"]
                    email = form_obj.cleaned_data['email']
                    phone=form_obj.cleaned_data['phone']
                    password=make_password(password)
                    user=User(username=username,password=password,email=email,reg_time=regtime,phone=phone)
                    user.save()
                    print('保存成功!')
                    print(form_obj.errors)
                    return render(request, 'app/index.html',locals())
                else:
                    # 如果验证失败则继续验证
                    err_msg=form_obj.errors
                    print(err_msg)
                    msg='验证码错误'
                    print('验证失败!')
                    return render(request, 'app/signup.html', locals())
    return render(request, 'app/signup.html', locals())




# 用户设置
def settings(request):
    path = catch_photo(request)
    username=request.session.get('username')
    if username:
        user1=User.objects.get(username=username)
        return  render(request,'app/form-validation.html',locals())
    return render(request,'app/form-validation.html',locals())




# 退出登录
def exit(request):
    request.session.flush()
    path = catch_photo(request)
    return render(request,'app/index.html',locals())




# 获取随机颜色
def get_random_color():
 R = random.randrange(255)
 G = random.randrange(255)
 B = random.randrange(255)
 return (R, G, B)


# 验证码
def get_verify_img(request):
    code_str=''
    # 定义画布背景颜色
    bg_color = get_random_color()
    # 画布大小
    img_size = (130, 40)
    # 定义画布
    image = Image.new("RGB", img_size, bg_color)
    # 定义画笔
    draw = ImageDraw.Draw(image, "RGB")
    # 创建字体（字体的路径）
    font_path = '/App/方正粗黑宋简体.ttf'
    # 实例化字体，设置大小是30
    font = ImageFont.truetype(font_path, 20)
    # 准备画布上的字符集
    source = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"
    # 保存每次随机出来的字符
    for i in range(4):
        # 获取数字随机颜色
        text_color = get_random_color()
        # 获取随机数字 len
        tmp_num = random.randrange(len(source))
        # 获取随机字符 画布上的字符集
        random_str = source[tmp_num]
        # 将每次随机的字符保存（遍历） 随机四次
        code_str += random_str
        # 将字符画到画布上
        draw.text((10 + 30 * i, 20), random_str, text_color, font)
    # 记录给哪个请求发了什么验证码
    request.session['code'] = code_str
    # 获得一个缓存区
    buf = io.BytesIO()
    # 将图片保存到缓存区
    image.save(buf, 'png')
    # 将缓存区的内容返回给前端 .getvalue 是把缓存区的所有数据读取
    return HttpResponse(buf.getvalue(),'image/png')


# 修改用户信息
def modify_infor(request):
    path = catch_photo(request)
    if request.method=='POST':
        # 从seesion获取用户名
        username=request.session.get('username')
        inp_user=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        if username:
            if email and phone:
                # 上传头像
                photo=request.FILES.get('photo')
                # 如果格式正确则上传
                if (check_file_type(photo.name) and check_file_size(photo.size)):
                    user=User.objects.get(username=username)
                    user.avatar=photo
                    user.email = email
                    user.phone = phone
                    user.save()
                    path= "uplod/" + str(user.avatar)
                    print(path)
                else:
                    return HttpResponse('类型错误或者大小超出限制')
            else:
                path='/static/images/2.jpg'
                return render(request,'app/form-validation.html',locals())
        else:
            # 如果未登录则跳转登录
            return render(request,'app/signin.html',locals())
        # 上传成功跳转首页
        return render(request,'app/index.html',locals())


# 文件上传类型检查
def check_file_type(filename):
        ext = os.path.splitext(filename)
        if ext and len(ext) > 1:
            # 获取后缀
            ext = ext[1].strip('.')  # 去掉.
        else:
            return False
        return ext.lower() in PHOTO_STYLE


# 文件上传大小检查
def check_file_size(fileSize):
    return fileSize<MAX_FILE_SIZE


# 解封
def activate_user(request):
    return None




# 用户反馈
def user_response(request):
    path = catch_photo(request)
    if request.method=='POST':
        username = request.session.get('username')
        input_name=request.POST.get('name')
        email=request.POST.get('mail')
        sub=request.POST.get('top')
        suggest=request.POST.get('suggestion')
        print(input_name,email,sub,suggest)
        if username:
            user=User_Response()
            user.username=input_name
            user.email=email
            user.subject=sub
            user.suggest=suggest
            user.save()
            print('保存成功')
            return render(request,'app/index.html',locals())
        else:
            return render(request,'app/signin.html',locals())
    return render(request,'app/form-validation.html')



# 积分兑换
def rewards_points(request,mid='1'):
    path1=request.get_full_path()
    path=catch_photo(request)
    # 获取musicid
    mid=re.match(r'/[\w_]+/(\d+)/$', path1).group(1)
    # 查询出兑换的歌曲数据
    # music是一个queryset对象
    # music=Music.objects.filter(id=mid).defer('music_list_id')
    music=Music.objects.defer('music_list_id').get(id=mid)
    username=request.session.get('username')

    if username:
        # 查询出当前用户
        user=User.objects.get(username=username)
        if user.score>music.score:
            user.score-=music.score
            user.save()
            # 用户积分兑换
            users=models.Orders.objects.create(music=music,music_user=user)
            users.save()
            success='兑换成功'
            print(success)
            pager = list_page(page=1)
            return render(request, 'app/index.html', {'success':success,'path':path,'pager':pager})
        else:
            err='用户积分不足'
            pager=list_page(page=1)
            return render(request,'app/shop.html',{'err':err,'path':path,'pager':pager})
    else:
        return render(request,'app/signin.html',locals())
