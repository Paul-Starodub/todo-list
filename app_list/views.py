from django.urls import reverse_lazy
from django.views import generic

from app_list.models import Task, Tag


class IndexView(generic.ListView):
    queryset = Task.objects.prefetch_related("tags")
    template_name = "app_list/index.html"


class TagView(generic.ListView):
    queryset = Tag.objects.prefetch_related("tasks")


class TagCreateView(generic.CreateView):

    model = Tag
    fields = "__all__"
    template_name = "app_list/tag_form.html"
    success_url = reverse_lazy("app_list:tag-list")


class TagUpdateView(generic.UpdateView):

    model = Tag
    fields = "__all__"
    template_name = "app_list/tag_form.html"
    success_url = reverse_lazy("app_list:tag-list")


class TagDeleteView(generic.DeleteView):

    model = Tag
    success_url = reverse_lazy("app_list:tag-list")
