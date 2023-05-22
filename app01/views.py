from django.shortcuts import render

from app01 import models


# Create your views here.

def show_index(request):
    """
    :param request:
    :return: 显示 index页面函数
    """
    return render(request, 'index.html')
