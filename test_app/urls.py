from django.urls import path

from test_app.views import HellowView


urlpatterns = [
    path('hello/', HellowView.as_view()),
]
