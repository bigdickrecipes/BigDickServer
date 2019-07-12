from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from salsa.models import Recipes
import json

# Create your views here.

@csrf_exempt
def create_recipe(request):
    if request.method == 'GET':
        return HttpResponse('this is a get')
    if request.method == 'POST':
        body = json.loads(request.body)
        print('this is the print: ', body)
        new_recipe = Recipes(title = body['title'])
        new_recipe.save()
        return HttpResponse('got it')