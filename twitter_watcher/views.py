from django.shortcuts import render
from django.http import HttpResponse
from twitter_api import api

# Create your views here.
def index(request):
    #r = requests.get(url, headers=headers, proxies=os.environ.get("PROXIES"))
    response = api.api_call('get_status', 327926550815207424)

    return HttpResponse(response.text)