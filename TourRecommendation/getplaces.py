# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 13:43:44 2022

@author: Studio Pc-1
"""

# Importing required libraries
from googleplaces import GooglePlaces, types, lang
import requests
import json

API_KEY = 'AIzaSyDwaXa3JZsFqv71812tm1k5FokRzLrX0RM'

google_places = GooglePlaces(API_KEY)

query_result = google_places.nearby_search(
        lat_lng ={'lat': 19.157934, 'lng': 72.993477},
        radius =300,
        types =[types.TYPE_GYM])

# If any attributions related
# with search results print them
if query_result.has_attributions:
    print (query_result.html_attributions)

bank = []
# Iterate over the search results
for place in query_result.places:
    bank.append(place.name)
    
print(bank)
