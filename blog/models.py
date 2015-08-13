from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=140)
    resume = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/', blank=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='blog')
    url = models.SlugField(max_length=140, blank=True)

    def save(self, *args, **kwargs):
        print self
        if not self.id:
            self.url = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
