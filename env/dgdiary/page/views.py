from django.shortcuts import render,get_object_or_404
from .models import Page
from .forms import PageForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def create(request):

	form = PageForm(request.POST or None,request.FILES or None)
	context = {
		"title":"How was your day?",
		"form":form,
		"button":"Submit"
	}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Congratulations!! Your input has been saved.")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request,"Something went wrong!!")
	return render(request, "create.html", context)

def list(request):
	queryset = Page.objects.all()
	context = {
		'queryset': queryset,
	}
	return render(request, 'list.html', context)

def detail(request,id):
	query = get_object_or_404(Page,id=id)
	context = {
		"query":query,
	}
	return render(request, "detail.html", context)

def update(request,id=None):
	query = get_object_or_404(Page,id=id)
	form = PageForm(request.POST or None,request.FILES or None,instance = query)
	context = {
		"query":query,
		"form":form,
		"button":"Submit",
		"title":"How was your day?",
	}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Congratulations!!! Your input has been updated.")
		return HttpResponseRedirect(query.get_absolute_url())
	return render(request, "create.html", context)