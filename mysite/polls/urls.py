from django.urls import path

from . import views

# Application Namespace url define
app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
]