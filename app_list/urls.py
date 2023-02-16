from django.urls import path

from app_list.views import (
    IndexView,
    TagView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

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
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="task-delete"
    ),

]

app_name = "app_list"
