from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.core.context_processors import csrf
from quizapp.models import quiz
# Create your views here.

def home(request):
	args={}
	args['p']	=	'home'
	args['next_url']	=	'/rules/'
	args['pre_v']	=	None
	args['sol']	=	None
	return render(request,'home.html',args)

def keepcalm(request):
	args={}
	args['p']	=	'keepcalm'
	args['next_url']='/screening/true/1/'
	args['pre_v']	= '/screening/false/3'
	args['sol']	=	None
	return render(request,'home.html',args)

def screening(request,qno='1',ans='false'):
	args={}
	count	=	quiz.objects.all().count()
	args['p']	=	'screeni'
	if ans=='false':
		args['screening']=True
		if int(qno) == count:
			args['next_url']='/keepcalm/'
		else:
			if int(qno)==1:
				args['pre_v']='/marking/'
			else:
				args['pre_v']='/screening/false/'+str(int(qno)-1)+'/'
			args['next_url']='/screening/false/'+str(int(qno)+1)+'/'

	elif ans=='true':
		args['screening']=False
		if int(qno) == count:
			args['next_url']='/'# change to end page...
		else:
			if int(qno)==1:
				args['pre_v']='/keepcalm/'
			else:
				args['pre_v']='/screening/true/'+str(int(qno)-1)+'/'
			args['next_url']='/screening/true/'+str(int(qno)+1)+'/'
	result	=	quiz.objects.get(Position=int(qno))
	# result.Displaytime=50
	# result.save()
	args['result']=result
	return render(request,'screening.html',args)



def welcome(request):
	pass # 
def sample(request):
	pass



def rules(request):
	args={}
	args['p']	=	'rules'
	args['next_url']='/marking/'
	args['pre_v']	=	'/'
	return render(request,'rules_regulation.html',args)
def marking(request):
	args={}
	args['p']	=	'marking'
	args['pre_v']	=	'/rules/'
	args['next_url'] = '/screening/false/1'
	return render(request,'marking.html',args)
