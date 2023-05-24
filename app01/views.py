from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils import Public_Function


# Create your views here.

def show_index(request):
    """
    :param request:
    :return: 显示 index页面函数
    """
    return render(request, 'index.html')


@csrf_exempt
def user_register(request):
    """
    :param request:
    :return: 用户注册函数
    """
    user_name = request.POST.get("user_name")
    user_mobile = request.POST.get("user_mobile")
    user_password = request.POST.get("user_password")
    # 判断数据是否存在，存在返回True 不存在返回False
    exists = models.user.objects.filter(user_mobile=user_mobile).exists()
    data = {
        "user_name": user_name,
        "user_mobile": user_mobile,
        "user_password": user_password,
        "create_time": Public_Function.format_time()
    }
    if not exists:
        models.user.objects.create(**data)
        return JsonResponse({"status": True, "data": "注册成功!"})
    return JsonResponse({"status": False, "data": "注册失败，该手机号已注册!"})


@csrf_exempt
def user_login(request):
    """
    :param request:
    :return: 用户登录函数
    """
    user_mobile = request.POST.get("user_mobile")
    user_password = request.POST.get("user_password")
    # 判断数据是否存在，存在返回True 不存在返回False
    exists = models.user.objects.filter(user_mobile=user_mobile, user_password=user_password).exists()
    if exists:
        return JsonResponse({"status": True, "data": "登录成功！"})
    return JsonResponse({"status": False, "data": "用户名或密码错误！"})


def home_page(request):
    """
    :param request:
    :return: 显示 home_page页面函数
    """
    return render(request, 'home_page.html')