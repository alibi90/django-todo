from datetime import datetime

from django.shortcuts import render, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.urls import reverse

from .models import TodoItem

# def index(request):
# 	all_todos = TodoItem.objects.all()
# 	import pdb; pdb.set_trace()
# 	return render(request, 'todo/index.html', {"todos": all_todos})

# class IndexView(generic.ListView):
# 	# model = TodoItem
# 	template_name = 'todo/index.html'
# 	context_object_name = 'todos'

# 	def get_queryset(self):
# 		return TodoItem.objects.all()


class IndexView(View):

	def get(self, request):
		all_todos = TodoItem.objects.all()
		return render(request, 'todo/index.html', {"todos": all_todos})


class AddTodoView(View):

	def get(self, request):
		return render(request, 'todo/add.html')

	def post(self, request):
		TodoItem.objects.create(
			title=request.POST['title'],
			content=request.POST['content'],
			due_date=datetime.now())
		# all_todos = TodoItem.objects.all()
		return redirect('/todo')


class AddTodoViewCreate(CreateView):
	model = TodoItem
	fields = ['title', 'content', 'due_date']

	def get_success_url(self):
		return reverse('todo:todo-index')
