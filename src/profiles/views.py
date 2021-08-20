from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Profile



# Create your views here.


def test_view(request):
	if request.user.is_authenticated:
		user= request.user
		print(user)
		#profile=Profile.objects.get(user=user)
		profile=get_object_or_404(Profile, user=user)
	else:
		profile= 'no profile'

	context={

	'user':profile
	}

	return render(request, 'profiles/test.html',context)