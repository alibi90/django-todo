from django.shortcuts import render, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from .models import TodoItem

# def index(request):
# 	+all_todos = TodoItem.objects.all()
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


# def addTodo(request):

# 	if request.method == "POST":
# 		import pdb; pdb.set_trace()
# 		title = request.POST['title']
# 		content = request.POST['content']
# 		due_date = request.POST['due_date']

# 		TodoItem.objects.create(title=title, content=content, due_date=due_date)

# 		return redirect('/todo')
# 	elif request.method == "GET":
# 		return render(request, 'todo/add.html')

class AddTodoCreate(CreateView):
    model = TodoItem
    fields = ['title', 'content', 'due_date']

    def get_success_url(self):
        return reverse('todo:index')


class UpdateTodo(UpdateView):
    model = TodoItem
    fields = ['title', 'content', 'due_date']

    def get_success_url(self):
        return reverse('todo:index')
