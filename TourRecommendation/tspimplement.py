from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = dist_matrix
    data['city_names'] = places
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def print_solution(manager, routing, assignment):
    """Prints assignment on console."""
    print('Total distance: {} meters'.format(assignment.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Index:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = assignment.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Route distance: {}miles\n'.format(route_distance)
    
    
def return_indexes(routing, assignment):
    index = routing.Start(0)
    indexes = []
    while not routing.IsEnd(index):
        previous_index = index
        index = assignment.Value(routing.NextVar(index))
        indexes = np.append(indexes, index)
    return indexes


def distance_callback(from_index, to_index):
    """Returns the distance between the two nodes."""
    # Convert from routing variable Index to distance matrix NodeIndex.
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distance_matrix'][from_node][to_node]


places = ['koparkhairane', 'thane', 'turbhe', 'juinagar', 'Airoli']

# the region
Location='Airoli'
# choose a mode
Mode = "walking"  # "driving", "walking", "bicycling", "transit"
# get Google API key from following website: 
password = "AIzaSyDwaXa3JZsFqv71812tm1k5FokRzLrX0RM"

import numpy as np
import googlemaps
import json

from GoogleMaps import *


lat = []
lng = []

google_maps = GoogleMaps(password)
for place in places:
    # print(place)
    result = google_maps.get_address_recommendation(query=place, language='en', location=Location)
    lat = np.append(lat, result[0]["lat"])
    lng = np.append(lng, result[0]["lng"])
lat = lat.astype(float)
lng = lng.astype(float)
# lat, lng

# print(lat)
# print(lng)

gmaps = googlemaps.Client(key=password)

dist_matrix = []

for i in range(len(places)):
    for j in range(len(places)):
        x = (lat[i], lng[i])
        y = (lat[j], lng[j])
        directions_result = gmaps.directions(x,y,
                                    mode=Mode,
                                    avoid="ferries",
                                    )
        dist_matrix.append(directions_result[0]['legs'][0]['distance']['value'])
dist_matrix = np.reshape(dist_matrix, (len(places), len(places)))
# dist_matrix.astype(int)

dist_matrix = np.asmatrix(dist_matrix)

for i in range(0, len(places), 1):
    for j in range(i+1, len(places), 1):
        dist_matrix[j,i] = dist_matrix[i,j]
dist_matrix = np.asarray(dist_matrix)

# print(dist_matrix)

"""Entry point of the program."""
# Instantiate the data problem.
data = create_data_model()

# Create the routing index manager.
manager = pywrapcp.RoutingIndexManager(
    len(data['distance_matrix']), data['num_vehicles'], data['depot'])

# Create Routing Model.
routing = pywrapcp.RoutingModel(manager)

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Define cost of each arc.
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem.
assignment = routing.SolveWithParameters(search_parameters)

# Print solution on console.
if assignment:
    print_solution(manager, routing, assignment)
    indexes = return_indexes(routing, assignment)
print(type(indexes))
list1 = indexes.tolist()

myList = [round(x) for x in list1]
myList.pop()
print(myList)
