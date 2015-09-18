from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import requests as req
import json
from rauth import OAuth2Service

# Create your views here.
def main(request):

    uber_api = OAuth2Service(
     client_id='QJp6IKuubwBoXvIbtfRTWMzAhW931bX9',
     client_secret='eMdSYjGQE_01JqgE48FpLLZFyxL6VSaBiJuYOHMz',
     name='INFOVIS',
     authorize_url='https://login.uber.com/oauth/authorize',
     access_token_url='https://login.uber.com/oauth/token',
     base_url='https://api.uber.com/v1/',
     )

    parameters = {
        'response_type': 'code',
        'scope': 'profile',
        'redirect_uri': 'http://localhost:8000/redirect_url/',
    }

    # Redirect user here to authorize your application
    login_url = uber_api.get_authorize_url(**parameters)
    print login_url
    r = req.get(login_url)
    print r
    print r.status_code

    return render_to_response('d3tutorial.html', RequestContext(request))


def products(request):
    url = 'https://api.uber.com/v1/products'
    parameters = {
    'server_token': 'tBSlsqwP7AfaBIZfHDjd2nASkGDfuHmenwnBFznj',
    'latitude': 33.775618,
    'longitude': -84.396285,
    }

    response = requests.get(url, params=parameters)

    data = response.json()
    print data

    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")

def product(request):

    product_id = request.GET['product_id']

    url = 'https://api.uber.com/v1/products/' + product_id
    print url
    parameters = {
    'server_token': 'tBSlsqwP7AfaBIZfHDjd2nASkGDfuHmenwnBFznj',
    'product_id': product_id
    }

    response = requests.get(url, params=parameters)

    data = response.json()
    print data

    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")


def price(request):
    url = 'https://api.uber.com/v1/estimates/price'
    parameters = {
    'server_token': 'tBSlsqwP7AfaBIZfHDjd2nASkGDfuHmenwnBFznj',
    'start_latitude': 33.775618,
    'start_longitude': -84.396285,
    'end_latitude': 33.783768,
    'end_longitude': -84.371889,
    }

    response = requests.get(url, params=parameters)

    data = response.json()
    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")

def time(request):
    url = 'https://api.uber.com/v1/estimates/time'
    parameters = {
    'server_token': 'tBSlsqwP7AfaBIZfHDjd2nASkGDfuHmenwnBFznj',
    'start_latitude': 33.775618,
    'start_longitude': -84.396285,

    }

    response = requests.get(url, params=parameters)

    data = response.json()
    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")


def redirect_url(request):
    print "redirect_url"

    parameters = {
    'redirect_uri': 'INSERT_ROUTE_TO_STEP_TWO',
    'code': request.args.get('code'),
    'grant_type': 'authorization_code',
    }

    response = requests.post(
        'https://login.uber.com/oauth/token',
        auth=(
            'INSERT_CLIENT_ID',
            'INSERT_CLIENT_SECRET',
        ),
        data=parameters,
    )

    # This access_token is what we'll use to make requests in the following
    # steps
    access_token = response.json().get('access_token')
    return render_to_response('d3tutorial.html', RequestContext(request))


def me(request):
    response=''
    data = response.json()
    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")

def history(request):
    response=''
    data = response.json()
    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")

def requests(request):
    response=''
    data = response.json()
    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")

