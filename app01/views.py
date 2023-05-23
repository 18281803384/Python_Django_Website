from django.http import JsonResponse
from django.shortcuts import render
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
    user_name = request.POST.get("user_name")
    user_mobile = request.POST.get("user_mobile")
    user_password = request.POST.get("user_password")
    exists = models.user.objects.filter(user_mobile=user_mobile).exists()
    data = {
        "user_name": user_name,
        "user_mobile": user_mobile,
        "user_password": user_password,
        "create_time": Public_Function.format_time()
    }
    if not exists:
        models.user.objects.create(**data)
        return JsonResponse({"status": True, "data": "注册成功！"})
    return JsonResponse({"status": False, "data": "该手机号已注册！"})
