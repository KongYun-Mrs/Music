import re
from django.forms import widgets
from django import forms
from django.http import request
# from App.views import code_str
from App.models import User


class RegForms(forms.Form):
    # captcha = CaptchaField()
    username = forms.CharField(
        label="帐号",
        max_length=16,
        min_length=4,
        # 自定义类的属性
        widget=widgets.TextInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "帐号不能为空"
        }
    )

    # 调用form组件内部方法创建一个长度不大于12且不小于3的密码文本框
    password = forms.CharField(
        label="密码",
        max_length=12,
        min_length=3,
        # 定义为密码文本,render_value设置为验证不通过时不把密码刷新掉
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于3位数",
            "required": "密码不能为空"
        }
    )

    email=forms.EmailField(
        label='邮箱',
        max_length=20,
        min_length=3,
        error_messages={
            'invailed':'邮箱格式错误',
            'required':'邮箱不能为空'
        }
    )

    phone = forms.CharField(
        label="手机号",
        max_length=11,
        min_length=3,
        error_messages={
            "required": "手机号不能为空"
        }
    )

    code=forms.CharField(
        label='验证码',
        error_messages={
            'required':'验证码不能为空'
        }
    )


    def clean(self):
        cleaned_data = super(RegForms, self).clean()
        username = cleaned_data.get('username')
        password=cleaned_data.get('password')
        phone=cleaned_data.get('phone')
        code = cleaned_data.get("yzm")#用户输入
        if User.objects.filter(username=username).exists():
            msg = '用户名已存在'
            self._errors['username'] = self.error_class([msg])
            del cleaned_data['username']

        elif  re.match(r'^\d+$',password):
            msg = ('密码不能是纯数字')
            self._errors['password'] = self.error_class([msg])
            del cleaned_data['password']

        elif not re.match(r'1[3,5,7,8,9][\d]{9}$',phone):
            msg = ('手机号不正确')
            self._errors['phone'] = self.error_class([msg])
            del cleaned_data['phone']
        return cleaned_data


