from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

def search_it(request):
    import requests
    if 'location' in request.GET:
        city = request.GET.get('location')

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}"

        # demonstrate how to use the 'params' parameter:
        x = requests.get(url, params={"appid": "ead9aa9cf0f190268f8780cc1374ff1a"})

        #Converts response object to dictionary
        x = x.json()

        context = {
            'weather_condition': f"Weather Condition - {x['weather'][0]['main'].upper()}",
            'weather_description': f"Weather Description - {x['weather'][0]['description'].upper()}",
            'country': f"Country - {x['sys']['country'].upper()}",
            'city':  f"City - {x['name'].upper()}",
            'temp':  f"Temperature - {x['main']['temp']}",
            'base': f"Base - {x['base'].upper()}"
        }

        return render(request, 'frontend/home.html', context)
    return render(request, 'frontend/home.html')
