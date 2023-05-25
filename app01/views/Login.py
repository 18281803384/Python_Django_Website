from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO

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
    if exists:
        return JsonResponse({"status": False, "data": "注册失败，该手机号已注册!"})
    data = {
        "user_name": user_name,
        "user_mobile": user_mobile,
        "user_password": user_password,
        "create_time": Public_Function.format_time()
    }
    # 执行创建表内数据
    models.user.objects.create(**data)
    return JsonResponse({"status": True, "data": "注册成功!"})


@csrf_exempt
def user_login(request):
    """
    :param request:
    :return: 用户登录函数
    """
    # 获取ajax请求中的数据
    user_mobile = request.POST.get("user_mobile")
    user_password = request.POST.get("user_password")
    # 获取用户输入的验证码字符串
    user_code = request.POST.get("user_code")
    # 获取正确的图片验证码字符串
    code = request.session.get('image_code', '')
    if user_code != code:
        return JsonResponse({"status": False, "data": "验证码错误！"})
    # 根据条件查询表内数据
    row_data = models.user.objects.filter(user_mobile=user_mobile, user_password=user_password).first()
    # 如果没有数据
    if not row_data:
        return JsonResponse({"status": False, "data": "用户名或密码错误！"})
    # 数据库存在数据的话，则继续执行语句
    request.session["info"] = {'id': row_data.id, 'user_name': row_data.user_name, 'user_mobile': row_data.user_mobile}
    # 设置session超时 1天免登陆
    request.session.set_expiry(60 * 60 * 12 * 1)
    return JsonResponse({"status": True, "data": "登录成功！"})


@csrf_exempt
def change_password(request):
    # 获取ajax请求中的数据
    user_mobile = request.POST.get("user_mobile")
    user_password = request.POST.get("user_password")
    # 根据条件查询表内数据
    data_row = models.user.objects.filter(user_mobile=user_mobile).first()
    # 如果没有数据
    if not data_row:
        return JsonResponse({"status": False, "data": "修改失败！手机号不存在，请刷新再试。"})
    # 数据库存在数据的话，则继续执行语句
    models.user.objects.filter(user_mobile=user_mobile).update(user_password=int(user_password))
    return JsonResponse({"status": True, "data": "修改成功！"})


# 获取图片验证码
def image_code(request):
    # 调用pillow函数，生成图片
    img,code_string = Public_Function.check_code()

    # 写入到自己的session中（以便于后续获取验证码再进行校验）
    request.session['image_code'] = code_string
    # 给session设置60s后超时
    request.session.set_expiry(60)

    # 写入内存(Python3)
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())