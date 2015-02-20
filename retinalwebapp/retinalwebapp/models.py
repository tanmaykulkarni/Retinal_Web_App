from django.db import models

# defining models here...
class User(models.Model):
  def __unicode__(self):
    return self.name
  name = models.CharField(max_length=100)	# the name of the user
  institute = models.CharField(max_length=200)	# the institution that the doctor belongs to (default LVP)
  email = models.EmailField(max_length=200)	# the email of the doc
  password = models.CharField(max_length=10)	# password
