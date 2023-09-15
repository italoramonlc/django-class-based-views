from django.urls import path
from .views import HomeRedirectView

app_name = "core"
urlpatterns = [
    path("",HomeRedirectView.as_view(),name="home"),
]