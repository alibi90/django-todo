from django.shortcuts import render
from django.views import generic

from .models import TodoItem

# def index(request):
# 	all_todos = TodoItem.objects.all()
# 	import pdb; pdb.set_trace()
# 	return render(request, 'todo/index.html', {"todos": all_todos})

class IndexView(generic.ListView):
	# model = TodoItem
	template_name = 'todo/index.html'
	context_object_name = 'todos'

	def get_queryset(self):
		return TodoItem.objects.all()
