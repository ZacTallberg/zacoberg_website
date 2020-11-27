from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class KittenImage(models.Model):
    file=models.ImageField(upload_to="kitten")
    description=models.CharField(max_length=100, blank=True, null=False, default='')

class FlowerImage(models.Model):
    file=models.ImageField(upload_to="flower")
    description=models.CharField(max_length=100, blank=True, null=False, default='')