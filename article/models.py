from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
      return self.name

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey('Category',blank=True,null=True)
    def __str__(self):
      return self.title