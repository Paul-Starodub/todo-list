from django.urls import path

from app_list.views import IndexView

urlpatterns = [
    path(
        "",
        IndexView.as_view(),
        name="index"
    ),
]

app_name = "app_list"
