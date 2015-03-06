from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404

import stakeholders
import initiatives
import sys
import json

# Create your views here.
def index(request):
	context = {}#'latest_question_list': latest_question_list#}
	return render_to_response("index.html", context)
	
def recent_tweets(request):
	tweets = initiatives.discover_tweets(0)
	return HttpResponse(json.dumps(tweets))

# 	if request.is_ajax():
# 		try:
# 			tweets = initiatives.discover_tweets()
# 			return HttpResponse(json.dumps(tweets))
# 			#stakeholder = int(request.POST['stakeholder'])
# 		except KeyError:
# 			return HttpResponse('Error') # incorrect post
# 	else:
# 		raise Http404



def list_stakeholders():
	output = stakeholdesrs.list_friends()
	return HttpResponse(json.dumps(output))






