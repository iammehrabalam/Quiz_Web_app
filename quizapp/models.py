from django.db import models

# Create your models here.

class quiz(models.Model):
	Type_choice	=	(('Easy','Easy'),('Medium','Medium'),('Difficult','Difficult'))
	Type		=	models.CharField(max_length=20,choices=Type_choice, blank=True)
	Question	=	models.CharField(max_length=300)
	Option1		=	models.CharField(max_length=100)
	Option2		=	models.CharField(max_length=100)
	Option3		=	models.CharField(max_length=100)
	Option4		=	models.CharField(max_length=100)
	Answer		=	models.IntegerField(verbose_name="Answer ( Type Which option )",default='1')
	Description	=	models.CharField(max_length=500)
	Displaytime	=	models.IntegerField()
	Position	=	models.IntegerField()

	def __unicode__(self):
		return 'Question Position:: '+str(self.Position)
