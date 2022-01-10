from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve

from django.http import Http404

class CustomMiddlewareExample(MiddlewareMixin):
	
	def process_request(self, request):
		ip = request.META.get("REMOTE_ADDR")
		path = resolve(request.path).url_name
		if not ip == '10.0.2.2' and path =='post-list':
			raise Http404("no access for you")
		else:
			print("this path is ok") 
			return  None