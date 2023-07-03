from django.shortcuts import render
from django.views import View

from django.http import HttpResponse

# Create your views here.


# В качестве представлений используем классовое представление
class HellowView(View):

    # на запрос GET будет отрабатывать эта функция
    def get(self, request):
        # Функция, как обработчик должна возвращать Response
        # (from django.http import HttpResponse)

        html = f'<f1>Hello, World</h1>'
        return HttpResponse(html)