from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from app_list.models import Task, Tag


class IndexView(generic.ListView):
    queryset = Task.objects.prefetch_related("tags")
    template_name = "app_list/index.html"


class TaskCreateView(generic.CreateView):

    model = Task
    fields = "__all__"
    success_url = reverse_lazy("app_list:index")


class TaskUpdateView(generic.UpdateView):

    model = Task
    fields = "__all__"
    success_url = reverse_lazy("app_list:index")


class TaskDeleteView(generic.DeleteView):

    model = Task
    success_url = reverse_lazy("app_list:index")


class TagView(generic.ListView):
    queryset = Tag.objects.prefetch_related("tasks")


class TagCreateView(generic.CreateView):

    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("app_list:tag-list")


class TagUpdateView(generic.UpdateView):

    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("app_list:tag-list")


class TagDeleteView(generic.DeleteView):

    model = Tag
    success_url = reverse_lazy("app_list:tag-list")


class TagTaskListView(generic.ListView):

    model = Task
    fields = "__all__"
    success_url = reverse_lazy("app_list:index")

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return HttpResponseRedirect(
            reverse("app_list:index")
        )
