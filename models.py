from django.db import models

from django.utils import timezone 
import datetime


#from django.utils.encoding import python_2_unicode_compatible


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    #def__str__(self)
      #  return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
	#def __str__(self):
       # return self.choice_te

class RecipeInfo(models.Model):
	recipe_name = models.CharField(max_length=100)
	recipe_content = models.CharField(max_length=200)

	def __str__(self):
		return (self.recipe_name + " " + self.recipe_content)




#class Question(models.Model):
#	def was_published_recently(self):
#		return self.pub_date >=timezone.now() - datetime.timedelta(days=1)
#
#	def__str__(self)
#	return self.choice_text
#	question_text = models.CharField(max_length=200)
#	pub_date = models.DateTimeField('date published')
#
#class Choice(models.Model):
#	question = models.ForeignKey(Question, on_delete=models.CASCADE)
#	choice_text = models.CharField(max_length=200)
#	vote = models.IntegerField(default=0)

# Create your models here.
