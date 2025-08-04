from django.db import models

from django.contrib.auth.models import User





# Forum board app models
class ForumThread(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ForumPost(models.Model):
    thread = models.ForeignKey(ForumThread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user} on {self.thread}"
