from django.db import models

# Create your models here.

class Task_manager(models.Model):

    task = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    due_date = models.DateField()


    def __str__(self):
        return self.task
