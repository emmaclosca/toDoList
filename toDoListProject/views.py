from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
import logging

# to complete this to do list project I have used this video as guidance -> https://www.youtube.com/watch?v=GRz3pcU89qU&t=300s

# logger guidance -> https://medium.com/@torkashvand/a-comprehensive-guide-to-logging-in-django-e041f311bcb7#:~:text=Django's%20logging%20framework%20is%20built,entry%20point%20for%20logging%20messages.
logger = logging.getLogger("toDoListProject.views")


class Tasks(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()  # checks for incomplete tasks and counts them

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
            context['search_input'] = search_input
        return context


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'toDoListProject/task_detail.html'

    # This method secures the sensitive data
    def get(self, request, *args, **kwargs):
        task = self.get_object()

        # If the logged-in user is the owner of the task, the task details will become available
        if task.user == request.user:
            return super().get(request, *args, **kwargs)
        else:
            logger.warning("Unauthorized access attempt to task details")
            return redirect('unauthorized_access')


class AddTask(CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        logger.info("Task has been created")
        return super().form_valid(form)


class UpdateTask(UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        logger.info("Task has been updated")
        return super().form_valid(form)


class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

    def delete(self, request, *args, **kwargs):
        logger.info("Task has been deleted")
        return super().delete(request, *args, **kwargs)


class UserLogin(LoginView):
    template_name = 'toDoListProject/login.html'
    fields = '__all__'
    redirect_authenticated_user = False

    def get_success_url(self):
        logger.info("User has logged in")
        return reverse_lazy('tasks')


class UserSignUp(FormView):
    template_name = 'toDoListProject/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            logger.info("Account has been created")
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super().get(*args, **kwargs)

    def form_invalid(self, form):
        logger.warning("Error with credentials for user registration")
        return super().form_invalid(form)

