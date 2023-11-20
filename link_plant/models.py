from django.db import models

# Create your models here.

# Remember each class is a table in our db

# Profiles -> Links

class Profile(models.Model):
  BG_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('yellow', 'Yellow'),
  )
  # name, slug, bg_color
  name = models.CharField(max_length=100)
  slug = models.SlugField(max_length=100)
  bg_color = models.CharField(max_length=50, choices=BG_CHOICES)
  # link_set
  # model_set

  def __str__(self):
    return self.name
  
class Link(models.Model):
  # text, url, profile
  text = models.CharField(max_length=100)
  url = models.URLField()
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  #relational dbs
  #  many to many
  #  one to one
  #  many to one
  def __str__(self):
    return f"{self.text} | {self.url}"