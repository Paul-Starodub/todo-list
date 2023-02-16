from django.views import generic

from app_list.models import Task


class IndexView(generic.ListView):
    queryset = Task.objects.prefetch_related("tags")
    template_name = "app_list/index.html"
