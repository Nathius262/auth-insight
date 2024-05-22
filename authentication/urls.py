from django.urls import path
from .views import custom_login
import allauth.account.views

app_name = "authentication"

urlpatterns = [
    path('predict/login/', custom_login, name="login"),
    # path('signup/', signup_view, name="signup"),
    path("logout/", allauth.account.views.logout, name="logout"),
]
