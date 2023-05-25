from django.shortcuts import render


def home_page(request):
    """
    :param request:
    :return: 显示 home_page页面函数
    """

    return render(request, 'home_page.html')