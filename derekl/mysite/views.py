from django.shortcuts import render
import random

# Create your views here.

def index(req):
	greetings = ["Hello MTV, welcome to my crib!", "ようこそ！", "Nice to meet 'cha", "Welcome", "Error 404 Not Found                                                                                                       jk take a look around!"]

	return render(req, 'index.html', context={"greeting": random.choice(greetings)})