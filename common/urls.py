from django.urls import path

from common.views import DatetimeView, IndexView


urlpatterns = [
    path('datetime/', DatetimeView.as_view()),
    path('', IndexView.as_view())  #
]
