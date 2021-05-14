from django.db import models
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, ModelFormMixin
from .models import Task
from .forms import TaskForm
from django.views.generic import DeleteView, UpdateView, DetailView, ListView, CreateView
from django.core.paginator import EmptyPage, Paginator
from django.views.generic.edit import ModelFormMixin


# Create your views here.



class TaskListView(ListView, ModelFormMixin):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'
    ordering = ['-id']
    paginate_by = 5
    form_class = TaskForm

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        # Explicitly states what get to call:
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # When the form is submitted, it will enter here
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()
            # Here ou may consider creating a new instance of form_class(),
            # so that the form will come clean.

        # Whether the form validates or not, the view will be rendered by get()
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

class DetailTaskView(DetailView):
    model = Task
    template_name = 'detail.html'


class UpdateTaskView(UpdateView):
    model = Task
    fields = ['content']
    template_name = 'update.html'
    success_url = '/'


class DeleteTastView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = '/'


def searchTask(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        tasks = Task.objects.all().filter(content__contains=search)
        tasks2 = Task.objects.all().filter(date_created__contains=search)
        return render(request, 'searchtask.html', {'tasks':tasks, 'dates':tasks2})