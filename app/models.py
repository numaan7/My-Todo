from django.db import models

# Create your models here.
class Todo(models.Model):
    PRIORITY_CHOICES = [
    ('HP', 'High Priority'),
    ('MP', 'Medium Priority'),
    ('LP', 'Low Priority'),
    
]
    title=models.CharField(max_length=100)
    details=models.TextField()
    datetime=models.DateTimeField(auto_now_add=True)
    priority=models.CharField(max_length=2,choices=PRIORITY_CHOICES,default='MP')
    completed=models.BooleanField(default=False)
    def __str__(self):
        return self.title