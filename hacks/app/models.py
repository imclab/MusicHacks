from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Circle(models.Model):
  users = models.ManyToManyField(User, related_name='circle_users')
  title = models.CharField(max_length=63)
  teacher = models.ForeignKey(User, related_name='circle_teacher')
  description = models.TextField()
  due_date = models.TimeField()
  background_image = models.URLField()

class Inspiration(models.Model):
  url = models.URLField()
  circle = models.ForeignKey(Circle)
  title = models.CharField(max_length=300)

class Genre(models.Model):
  name = models.CharField(max_length=63)
  image = models.URLField()

  def __unicode__(self):
    return self.name

class Song(models.Model):
  time = models.TimeField(auto_now_add=True)
  user = models.ForeignKey(User, related_name='song_user')
  title = models.CharField(max_length=255)
  description = models.TextField()
  starred = models.ManyToManyField(User, related_name='song_starred')
  circle = models.ForeignKey(Circle)
  url = models.URLField()

class Comment(models.Model):
  song = models.ForeignKey(Song)
