from django.urls import path
from . import views

app_name = "about_us"
urlpatterns = [
	path("", views.index, name="index")
]