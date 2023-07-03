from django.urls import path

from login.views import loginView


urlpatterns = [
    path('login/', loginView.as_view())
]
