from django.shortcuts import render
from django.views import View
from datetime import datetime
from django.http import HttpResponse

# Create your views here.


# В качестве представлений используем классовое представление
class DatetimeView(View):

    # на запрос GET будет отрабатывать эта функция
    def get(self, request):
        # Функция, как обработчик должна возвращать Response
        # (from django.http import HttpResponse)

        html = f'{datetime.now()}'
        return HttpResponse(html)


class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')