from django.urls import path

from app_list.views import IndexView, TagView

urlpatterns = [
    path(
        "",
        IndexView.as_view(),
        name="index"
    ),
    path(
        "tags/",
        TagView.as_view(),
        name="tag-list"
    )
]

app_name = "app_list"
