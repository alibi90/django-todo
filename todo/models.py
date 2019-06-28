from django.db import models


class TodoItem(models.Model):
	todo_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	content = models.TextField()
	due_date = models.DateTimeField()

	def __str__(self):
		return self.title

