from django.db import models

from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User

class Author(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField()
    details = models.TextField()
    def __str__(self):
        return self.current_user.username

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Article(models.Model):
    article_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.FileField()
    paragraph = models.TextField()
    image_2 = models.FileField(blank=True)
    paragraph_2 = models.TextField(blank=True)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title

    # home page url
    def index_url(self):
        return reverse('blog:index')

    def blog_details_url(self):
        return reverse('blog:blog_details', kwargs={'id': self.id})

    def author_post_url(self):
        return reverse('blog:author_post', kwargs={'name': self.article_author.current_user.username})

class Comments(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()
    def __str__(self):
        return self.name