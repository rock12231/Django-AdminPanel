from faulthandler import disable
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)
