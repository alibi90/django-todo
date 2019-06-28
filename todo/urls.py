from django.conf.urls import url

# from .views import index
from .views import IndexView, AddTodoCreate, UpdateTodo

app_name = 'todo'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^add$', AddTodoCreate.as_view(), name="add"),
    url(r'^update/(?P<pk>\d+)/$', UpdateTodo.as_view(), name="update")
]
