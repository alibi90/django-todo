from django.conf.urls import url

# from .views import index
from .views import IndexView, AddTodoView, AddTodoViewCreate

app_name = 'todo'
urlpatterns = [
	url(r'^$', IndexView.as_view(), name="todo-index"),
	url(r'^add$', AddTodoView.as_view(), name="add-todo"),
	url(r'^add-todo$', AddTodoViewCreate.as_view(), name="add-todo-create"),
]