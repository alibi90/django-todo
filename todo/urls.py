from django.conf.urls import url

# from .views import index
from .views import IndexView

app_name = 'todo'
urlpatterns = [
	url(r'^$', IndexView.as_view(), name="index")
]