# dwitter/urls.py
from django.urls import path,include
from .views import dashboard,profile_list,profile,register
from django.views.generic.base import RedirectView
app_name = "dwitter"
urlpatterns = [
path("", dashboard, name="dashboard"),
path("dashboard/",RedirectView.as_view(url='/')),
path("profile_list/", profile_list, name="profile_list"),
path("profile/<int:pk>", profile, name="profile"),
path("accounts/", include("django.contrib.auth.urls")),
path("register/", register, name="register"),
]