from django.db import models

# Create your models here.
class Question(models.Model):
  def __unicode__(self):
    # return "Question " + str(self.id)
    return self.question_text
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

class Choice(models.Model):
  question = models.ForeignKey(Question)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
