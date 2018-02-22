from django.shortcuts import render
import random

# Create your views here.

def index(req):
	greetings = ["Wazzap", "Hello MTV, welcome to my crib!", "ようこそ！", "Nice to meet 'cha", "Welcome", "はじめまして!"]

	return render(req, 'index.html', context={"greeting": random.choice(greetings)})