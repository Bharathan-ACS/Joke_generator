from django.shortcuts import render
import requests
# Create your views here.
# import pyjokes

def home(request):
    # joke = pyjokes.get_joke(language="en",category="all")
    # d={'joke':joke}

    url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url)
    data = response.json()

    joke = data["setup"] + " " + data["punchline"]
    d={'joke':joke}
    return render(request,'home.html',d)