from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def test_view(request):
	if request.user.is_authenticated:
		user= request.user

	else:
		user= 'no user'

	context={

	'user':user
	}

	return render(request, 'profiles/test.html',context)