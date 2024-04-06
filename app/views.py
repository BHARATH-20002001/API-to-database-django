from django.shortcuts import render

# Create your views here.
from app.models import *
import requests

def get_population  ():
    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    response = requests.get(url)
    data = response.json()["data"]
    for country in data:
        if not Population.objects.filter(Country = country["Nation"],
                                        Year = country["Year"],
                                        Human_count = country["Population"]).exists():
            Population.objects.get_or_create(Country = country["Nation"],
                                            Year = country["Year"],
                                            Human_count = country["Population"])
            print("saved")
        else:
            print("data already existing")
        
        