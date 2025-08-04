from django.db import models



class Todo(models.Model):
    
    title = models.CharField(max_length=50)
    body = models.CharField(max_length =100)
    created_at = models.DateTimeField(auto_now_add = True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
