from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Status
from .forms import StatusForm
# Create your views here.


def status_create(request):
	if request.method == 'POST':
		form = StatusForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=True)
		context = {
			"form":form,
			"title":"So, how was your day?",
			"submit":"Submit"
		}
		return render(request, "create.html", context)
	else:
		context = {
		"title" : "See you tomorrow..",
		"submit":"Continue",
		}

def status_search(request,id):
	instance = get_object_or_404(Status,id=id);

	context = {
		"home" : "Buy",
		"instance" : instance,
	}
	return render(request, "search.html", context)

def status_home(request):
	queryset = Status.objects.all()
	context = {
		"home" : "Buy",
		"queryset":queryset,
	}
	return render(request, "home.html", context)