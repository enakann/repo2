from django.shortcuts import render
from django.http import HttpResponse
from kanap.forms import mod1Form

def index(request):
	dd=mod1Form(request.POST or None)
	if dd.is_valid():
		ss=dd.save()
		return HttpResponse("Form Submitted!")
		#return render(request,'base.html',{"dsvds":dd})
	context={
	"formaa":dd,
	}
	return render(request,'base.html',context)

# Create your views here.

