from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)


class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=False)


class Comments(models.Model):
    comments_id = models.AutoField(primary_key=True)
    text = models.TextField()
    blog_relation  = models.ForeignKey(Blog, on_delete=models.CASCADE, to_field='blog_id', related_name = "blog_relation")
