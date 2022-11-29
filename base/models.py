from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Article(models.Model):
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("article_content", kwargs={"slug": self.slug})

class Comment(models.Model):
    owner = models.ForeignKey(User,  on_delete=models.CASCADE)
    article =  models.ForeignKey(Article,  on_delete=models.CASCADE)
    body = models.CharField(max_length= 300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
    
    class Meta:
        ordering = ['-updated_at' ,'-created_at']

class Vote(models.Model):
    voted_by = models.ForeignKey(User,  on_delete=models.CASCADE , null=True)
    voted_on = models.ForeignKey(Article,  on_delete=models.CASCADE , null=True)
    up_vote = models.IntegerField(null=True, blank=True)
    down_vote = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.up_vote} {self.down_vote}'


# roadmap
class Roadmap(models.Model):
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Roadmap, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("roadmap_content", kwargs={"slug": self.slug})


class Roadmapsubtitle(models.Model):
    owner = models.ForeignKey(User,  on_delete=models.CASCADE)
    Roadmap =  models.ForeignKey(Roadmap,  on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sub_title
    
    class Meta:
        ordering = ['-updated_at' ,'-created_at']


class Link(models.Model):
    owner = models.ForeignKey(User,  on_delete=models.CASCADE)
    # Roadmap =  models.ForeignKey(Roadmap,  on_delete=models.CASCADE)
    sub_title =  models.ForeignKey(Roadmapsubtitle,  on_delete=models.CASCADE, null=True)
    link_field = models.CharField(max_length= 400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link_field
    
    class Meta:
        ordering = ['-updated_at' ,'-created_at']