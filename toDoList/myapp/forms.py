from django.forms import ModelForm
from myapp.models import Task_manager

class TaskForm(ModelForm):
    class Meta:
        model = Task_manager
        fields = '__all__'

