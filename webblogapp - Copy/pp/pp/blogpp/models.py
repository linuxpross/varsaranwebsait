from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    img = models.ImageField('img', upload_to='images/') 
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

class Message(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.author}: {self.text}'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.author}: {self.text}'
