from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Dating app models
class DatingProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=255)
    interested_in = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='dating_profiles/')

    def __str__(self):
        return self.user.username

class Match(models.Model):
    user1 = models.ForeignKey(User, related_name='user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='user2', on_delete=models.CASCADE)
    is_matched = models.BooleanField(default=False)
    match_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user1} & {self.user2}"
