from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question, RecipeInfo
from .forms import RecipeInfoForm, RecipeInfoDeleteForm, RecipeInfoFindForm

def index(request):
	if request.method == "POST":
		if 'submit' in request.POST:
			form = RecipeInfoForm(request.POST)
			if form.is_valid():
				post = form.save()
				return redirect('food:submit', pk=post.pk)
		elif 'delete' in request.POST:
			searchStr = RecipeInfoDeleteForm(request.POST)
			if searchStr.is_valid():
				f_name = searchStr.cleaned_data['recipe_name']
				RecipeInfo.objects.filter(recipe_name=f_name).delete()
				return redirect('food:delete')
		elif 'find' in request.POST:
			searchStr = RecipeInfoFindForm(request.POST)
			if searchStr.is_valid():
				f_name = searchStr.cleaned_data['recipe_name']
				return redirect('food:details', f_name)
	else:
		form = RecipeInfoForm()
		deleteform = RecipeInfoDeleteForm()
		findform = RecipeInfoFindForm()
	return render(request, 'food/index.html', {'form':form, 'deleteform':deleteform, 'findform':findform,})

def details(request, f_name):
	records = RecipeInfo.objects.filter(recipe_name=f_name)
	context = {'records':records}
	return render(request, 'food/detail.html', context)

def showAll(request):
	groups = RecipeInfo.objects.order_by('id')
	context = {'groups':groups}
	return render(request, 'food/showAll.html', context)

def submit(request, pk):
	post = get_object_or_404(RecipeInfo, pk = pk)
	return render(request, 'food/details.html', {'post':post})

def delete(request):
	return render(request, 'food/delete.html')

#def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    #return render(request, 'food/index.html', context

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'food/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'food/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

  	#return HttpResponseRedirect(reverse('food:results',args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'food/results.html', {'question': question})






















#
#from django.http import HttpResponse
#from .models import Question
#from django.template import loader
#
#from django.shortcuts import get_object_or_404, render
#from .models import Question
#from django.urls import reverse
#from django.http import HttpResponseRedirect, HttpResponse
#from django.http import HttpResponseRedirect
#from django.views import generic

#from .models import Choice, Question

#def detail(request, question_id):
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request, 'food/detail.html', { 'question': question})


#def detail(request, question_id):
#	try:
#		question = Question.objects.get(pk=question_id)
#	except Question.DoesNotExist:
#		raise Http404("question does not exist")
#	return render(request, ' food/detail.html', {'question' : question})

#def index(request):
#	latest_question_list = Question.object.order_by('-pub_date')[:5]
#	template = loader.get_template('food/index.html')
#	context = { 'latest_question_list': latest_question_list, } 

#output = ','.join([q.question_text for q in  latest_question_list]) 
#	return HttpResponse(template.render(context, request))

#def index(request, question):
#	return HttpResponse("Hello, World. hopefully this will be a project soon!")
# Create your views here.

#def detail(request, question_id):
#	return HttpsResponce(" youre looking at question %s." % question_id)

#def results(request, question_id):
#	response = "your looking at the results of question %s."
#	return HttpResponse(response % qiestopm_id)

#def vote(request, question_id):
#	return HttpResponse("your voting on question %s." %  question_#

#def vote(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    try:
#        selected_choice = question.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        
#        return render(request, 'food/detail.html', {
#            'question': question,
#            'error_message': "You didn't select a choice.",
#        })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
        
#        return HttpResponseRedirect(reverse('food:results', args=(question.id,)))

#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'food/results.html', {'question': question})


#class IndexView(generic.ListView):
#   template_name = 'food/index.html'
#    context_object_name = 'latest_question_list'

#    def get_queryset(self):
#        """Return the last five published questions."""
#        return Question.objects.order_by('id')[:5]


#class DetailView(generic.DetailView):
#    model = Question
#    template_name =' food/detail.html'


#class ResultsView(generic.DetailView):
#    model = Question
#    template_name = 'food/results.html'


#def vote(request, question_id):
    ... # same as above, no changes needed.
