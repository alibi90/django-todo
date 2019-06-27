from django.db import models


class TodoItem(models.Model):
	todo_id = models.IntegerField()
	title = models.CharField(max_length=200)
	content = models.TextField()
	due_date = models.DateTimeField()

	def __str__(self):
		return self.title

