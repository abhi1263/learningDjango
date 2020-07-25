from django.db import models


# Create your models here.
class Tasks(models.Model):
    task_title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    task_status = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title
