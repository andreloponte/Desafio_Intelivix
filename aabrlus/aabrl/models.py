from django.db import models

# Create your models here.
class Urls(models.Model):
    encurtamento_id = models.SlugField(max_length=6,primary_key=True)
    url_original = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    contador = models.IntegerField(default=0)
 
def __str__(self):
    return self.url_original
