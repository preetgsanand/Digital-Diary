from django.shortcuts import render,get_object_or_404
from .models import Page
from .forms import PageForm
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
		context = {
			"title":"See you tomorrow",
			"button":"Continue"
		}
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