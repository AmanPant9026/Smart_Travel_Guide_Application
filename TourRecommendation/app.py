
from flask import Flask
from flask import request
import pymysql

import json
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

from csv import writer

# from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import googlemaps

from GoogleMaps import *

# from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np

import scipy.stats

import scipy.spatial
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
from math import sqrt
import math
import warnings

app = Flask(__name__)

app.secret_key = 'any random string'

UPLOAD_FOLDER = 'static/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

warnings.simplefilter("error")


"---------------------------------------------------------------------------------------"

def dbConnection():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="root", database="tour_recommendation",port=3307)
        return connection
    except Exception as e:
        print(e)
        print("Something went wrong in database Connection")

def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")

con = dbConnection()
cursor = con.cursor()

"---------------------------------------------------------------------------------------"

cursor.execute('SELECT * FROM usertable')
maxid = cursor.rowcount

print(maxid+1)

users = maxid+1
items = 5
X=np.arange(0,10)


"---------------------------------------------------------------------------------------"

def readingFile(filename):
    f = open(filename,"r")
    data = []
    for row in f:
        r = row.split(',')
        e = [int(r[0]), int(r[1]), int(r[2])]
        data.append(e)
    return data

def similarity_user(data):
#     print ("Hello User 1")
    #f_i_d = open("sim_user_based.txt","w")
    user_similarity_cosine = np.zeros((users,users))
    user_similarity_jaccard = np.zeros((users,users))
    user_similarity_pearson = np.zeros((users,users))
    for user1 in range(users):
#         print (user1)
        for user2 in range(users):
            if np.count_nonzero(data[user1]) and np.count_nonzero(data[user2]):
                user_similarity_cosine[user1][user2] = 1-scipy.spatial.distance.cosine(data[user1],data[user2])
                user_similarity_jaccard[user1][user2] = 1-scipy.spatial.distance.jaccard(data[user1],data[user2])
                try:
                    if not math.isnan(scipy.stats.pearsonr(data[user1],data[user2])[0]):
                        user_similarity_pearson[user1][user2] = scipy.stats.pearsonr(data[user1],data[user2])[0]
                    else:
                        user_similarity_pearson[user1][user2] = 0
                except:
                    user_similarity_pearson[user1][user2] = 0

            #f_i_d.write(str(user1) + "," + str(user2) + "," + str(user_similarity_cosine[user1][user2]) + "," + str(user_similarity_jaccard[user1][user2]) + "," + str(user_similarity_pearson[user1][user2]) + "\n")
    #f_i_d.close()
    return user_similarity_cosine, user_similarity_jaccard, user_similarity_pearson

def crossValidation(data):
    k_fold = KFold(2,shuffle=False)

    Mat = np.zeros((users,items))
    for e in data:
        Mat[e[0]-1][e[1]-1] = e[2]

    sim_user_cosine, sim_user_jaccard, sim_user_pearson = similarity_user(Mat)
    #sim_user_cosine, sim_user_jaccard, sim_user_pearson = np.random.rand(users,users), np.random.rand(users,users), np.random.rand(users,users)

    '''sim_user_cosine = np.zeros((users,users))
    sim_user_jaccard = np.zeros((users,users))
    sim_user_pearson = np.zeros((users,users))

    f_sim = open("sim_user_based.txt", "r")
    for row in f_sim:
        r = row.strip().split(',')
        sim_user_cosine[int(r[0])][int(r[1])] = float(r[2])
        sim_user_jaccard[int(r[0])][int(r[1])] = float(r[3])
        sim_user_pearson[int(r[0])][int(r[1])] = float(r[4])
    f_sim.close()'''

    rmse_cosine = []
    rmse_jaccard = []
    rmse_pearson = []

    for train_indices, test_indices in k_fold.split(X):
        train = [data[i] for i in X[train_indices]]
        test = [data[i] for i in X[test_indices]]

        M = np.zeros((users,items))

        for e in train:
            M[e[0]-1][e[1]-1] = e[2]

        true_rate = []
        pred_rate_cosine = []
        pred_rate_jaccard = []
        pred_rate_pearson = []

        for e in test:
            user = e[0]
            item = e[1]
            true_rate.append(e[2])

            pred_cosine = 3.0
            pred_jaccard = 3.0
            pred_pearson = 3.0

            #user-based
            if np.count_nonzero(M[user-1]):
                sim_cosine = sim_user_cosine[user-1]
                sim_jaccard = sim_user_jaccard[user-1]
                sim_pearson = sim_user_pearson[user-1]
                ind = (M[:,item-1] > 0)
                #ind[user-1] = False
                normal_cosine = np.sum(np.absolute(sim_cosine[ind]))
                normal_jaccard = np.sum(np.absolute(sim_jaccard[ind]))
                normal_pearson = np.sum(np.absolute(sim_pearson[ind]))
                if normal_cosine > 0:
                    pred_cosine = np.dot(sim_cosine,M[:,item-1])/normal_cosine

                if normal_jaccard > 0:
                    pred_jaccard = np.dot(sim_jaccard,M[:,item-1])/normal_jaccard

                if normal_pearson > 0:
                    pred_pearson = np.dot(sim_pearson,M[:,item-1])/normal_pearson

            if pred_cosine < 0:
                pred_cosine = 0

            if pred_cosine > 5:
                pred_cosine = 5

            if pred_jaccard < 0:
                pred_jaccard = 0

            if pred_jaccard > 5:
                pred_jaccard = 5

            if pred_pearson < 0:
                pred_pearson = 0

            if pred_pearson > 5:
                pred_pearson = 5

#             print (str(user) + "\t" + str(  ) + "\t" + str(e[2]) + "\t" + str(pred_cosine) + "\t" + str(pred_jaccard) + "\t" + str(pred_pearson))
            pred_rate_cosine.append(pred_cosine)
            pred_rate_jaccard.append(pred_jaccard)
            pred_rate_pearson.append(pred_pearson)

        rmse_cosine.append(sqrt(mean_squared_error(true_rate, pred_rate_cosine)))
        rmse_jaccard.append(sqrt(mean_squared_error(true_rate, pred_rate_jaccard)))
        rmse_pearson.append(sqrt(mean_squared_error(true_rate, pred_rate_pearson)))

#         print (str(sqrt(mean_squared_error(true_rate, pred_rate_cosine))) + "\t" + str(sqrt(mean_squared_error(true_rate, pred_rate_jaccard))) + "\t" + str(sqrt(mean_squared_error(true_rate, pred_rate_pearson))))
        #raw_input()

    #print sum(rms) / float(len(rms))
    rmse_cosine = sum(rmse_cosine) / float(len(rmse_cosine))
    rmse_pearson = sum(rmse_pearson) / float(len(rmse_pearson))
    rmse_jaccard = sum(rmse_jaccard) / float(len(rmse_jaccard))

#     print( str(rmse_cosine) + "\t" + str(rmse_jaccard) + "\t" + str(rmse_pearson))

    f_rmse = open("rmse_user.txt","w")
    f_rmse.write(str(rmse_cosine) + "\t" + str(rmse_jaccard) + "\t" + str(rmse_pearson) + "\n")

    rmse = [rmse_cosine, rmse_jaccard, rmse_pearson]
    req_sim = rmse.index(min(rmse))

    print (req_sim)
    f_rmse.write(str(req_sim))
    f_rmse.close()

    if req_sim == 0:
        sim_mat_user = sim_user_cosine

    if req_sim == 1:
        sim_mat_user = sim_user_jaccard

    if req_sim == 2:
        sim_mat_user = sim_user_pearson

    #predictRating(Mat, sim_mat_user)
    return Mat, sim_mat_user


def predictRating(recommend_data):

    M, sim_user = crossValidation(recommend_data)

    f = open("tobe.csv","r")
    #f = open(sys.argv[2],"r")
    toBeRated = {"user":[], "item":[]}
    for row in f:
        r = row.split(',')    
        toBeRated["item"].append(int(r[1]))
        toBeRated["user"].append(int(r[0]))

    f.close()

    pred_rate = []

    #fw = open('result1.csv','w')
    # fw_w = open('result1.csv','w')

    l = len(toBeRated["user"])
    for e in range(l):
        user = toBeRated["user"][e]
        item = toBeRated["item"][e]

        pred = 3.0

        #user-based
        if np.count_nonzero(M[user-1]):
            sim = sim_user[user-1]
            #print("i got",sim)
                 
            ind = (M[:,item-1] > 0)
            #ind[user-1] = False
            normal = np.sum(np.absolute(sim[ind]))
                
            if normal > 0:
            
                pred = np.dot(sim,M[:,item-1])/normal

        if pred < 0:
            pred = 0

        if pred > 5:
            pred = 5

        pred_rate.append(pred)
        print (str(user) + "," + str(item) + "," + str(pred))
        #fw.write(str(user) + "," + str(item) + "," + str(pred) + "\n")
    return pred_rate

    M, sim_user = crossValidation(recommend_data)

    f = open("tobe.csv","r")
    #f = open(sys.argv[2],"r")
    toBeRated = {"user":[], "item":[]}
    for row in f:
        r = row.split(',')    
        toBeRated["item"].append(int(r[1]))
        toBeRated["user"].append(int(r[0]))

    f.close()

    pred_rate = []

    #fw = open('result1.csv','w')
    fw_w = open('result1.csv','w')

    l = len(toBeRated["user"])
    for e in range(l):
        user = toBeRated["user"][e]
        item = toBeRated["item"][e]

        pred = 3.0

        #user-based
        if np.count_nonzero(M[user-1]):
            sim = sim_user[user-1]
            #print("i got",sim)
                 
            ind = (M[:,item-1] > 0)
            #ind[user-1] = False
            normal = np.sum(np.absolute(sim[ind]))
                
            if normal > 0:
            
                pred = np.dot(sim,M[:,item-1])/normal

        if pred < 0:
            pred = 0

        if pred > 5:
            pred = 5

        pred_rate.append(pred)
        print (str(user) + "," + str(item) + "," + str(pred))
        #fw.write(str(user) + "," + str(item) + "," + str(pred) + "\n")
        fw_w.write(str(pred) + "\n")

    #fw.close()
    fw_w.close()

"---------------------------------------------------------------------------------------"

def create_data_model(dist_matrix,places):
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

def getTSPOutput(places):
    # places = flat_list
    print("places",places)
    
    Location='Airoli'
    # choose a mode
    Mode = "walking"  # "driving", "walking", "bicycling", "transit"
    # get Google API key from following website: 
    password = "AIzaSyDwaXa3JZsFqv71812tm1k5FokRzLrX0RM"
    
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
5    
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
    
    dist_matrix = np.asarray(dist_matrix)
    
    for i in range(0, len(places), 1):
        for j in range(i+1, len(places), 1):
            dist_matrix[j,i] = dist_matrix[i,j]
    dist_matrix = np.asarray(dist_matrix)
    
    # print(dist_matrix)
    
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(dist_matrix,places)
    
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
    
    myList.insert(0, 0)
    print(myList)
    
    return myList


"---------------------------------------------------------------------------------------"    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        print("GET")   

        username = request.form.get("username")
        passw = request.form.get("password")        
        email = request.form.get("emailid")
        mobile = request.form.get("mobilenumber")        
        print("INPUTS")        
        print("username",username)
        
        cursor.execute('SELECT * FROM usertable')
        maxid = cursor.rowcount
          
        list_data=[maxid+1,'3']
        
        cursor.execute('SELECT * FROM usertable WHERE username = %s', (username))
        count = cursor.rowcount
        if count == 1:            
            return "fail"
        else:  
            with open('tobe.csv', 'a', newline='') as f_object:  
                writer_object = writer(f_object)
                writer_object.writerow(list_data)  
                f_object.close()
            
            sql1 = "INSERT INTO usertable(username, email, mobile, password) VALUES (%s, %s, %s, %s);"
            val1 = (username, email, mobile, passw)
            cursor.execute(sql1,val1)
            con.commit()    
            
            sql2 = "INSERT INTO recomm(user_id, item_id, rating) VALUES (%s, %s, %s);"
            val2 = (int(maxid)+1, 1, 3.0)
            cursor.execute(sql2,val2)
            con.commit() 
            return "success"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        
        print("GET")        

        username = request.form.get("username")
        passw = request.form.get("password")       
        print("INPUTS")        
        print("username",username)
        
        cursor.execute('SELECT * FROM usertable WHERE username = %s AND password = %s', (username, passw))
        count = cursor.rowcount
        if count == 1:            
            return "success"
        else:
            return "fail"
        
"---------------------------------------------------------------------------------------"

@app.route('/getHotelData', methods=['GET', 'POST'])
def getHotelData():
    if request.method == 'POST':         
        
        username = request.form.get("username")
        print("I am in hotel")
        
        # cursor.execute('SELECT area FROM hotel_db WHERE rating >= %s',(ddd[userid]))
        # # cursor.execute('SELECT area FROM hotel_db')
        # row = cursor.fetchall()
        # print("BBBBBB",row)

        cursor.execute('SELECT area FROM hotel_db')
        row = cursor.fetchall()
        print("row",row)
        
        flat_list = []
        for sublist in row:
            for item in sublist:
                flat_list.append(item)
                
        myList = getTSPOutput(flat_list) 
        
        p=list()
        for i in myList:
            # print(flat_list[i])
            cursor.execute('SELECT * FROM hotel_db WHERE area = %s', (flat_list[i]))
            row = cursor.fetchall()
            a=row[0]
            p.append(a)
        print(p)        
                
        cursor.execute('SELECT id FROM usertable WHERE username = %s',(username))
        row = cursor.fetchall()
        c = int(row[0][0])

        print("row",row)

        # re_list=list()
        cursor.execute('SELECT * FROM recomm')
        row = cursor.fetchall()
            
        recommend_data = list(row)
        #recommend_data = readingFile(sys.argv[1])
        #crossValidation(recommend_data)
        print("recommend_data",recommend_data)
        ddd = predictRating(recommend_data)

        userid = c - 1
        print(userid)
        print("BBBBBB",ddd[userid])
        flval = format(ddd[userid], ".1f")
        print("BBBBBB",type(flval))
        df = pd.DataFrame(p, columns = ['a', 'b','c', 'd','e', 'f','g', 'h'])
        dfk1=df[df["d"]==float(flval)]
        dfk2=df[df["d"]!=float(flval)]
        dfk2 = dfk2.sort_values(by=['d'], ascending=False)
        frames2=[dfk1,dfk2]
        finaldf = pd.concat(frames2)  
        
        finallist = finaldf.values.tolist()
        
        jsonObj = json.dumps(finallist)   
        
        return jsonObj
    
@app.route('/getPlaceData', methods=['GET', 'POST'])
def getPlaceData():
    if request.method == 'POST': 
        
        username = request.form.get("username")
        print("I am in place")
                
        cursor.execute('SELECT area FROM place_db')
        row = cursor.fetchall()
        
        flat_list = []
        for sublist in row:
            for item in sublist:
                flat_list.append(item)
                
        myList = getTSPOutput(flat_list) 
        
        p=list() 
        for i in myList:
            # print(flat_list[i])
            cursor.execute('SELECT * FROM place_db WHERE area = %s', (flat_list[i]))
            row = cursor.fetchall()
            a=row[0]
            p.append(a)
        print(p)
        cursor.execute('SELECT id FROM usertable WHERE username = %s',(username))
        row = cursor.fetchall()
        c = int(row[0][0])

        print("row",row)

        # re_list=list()
        cursor.execute('SELECT * FROM recomm')
        row = cursor.fetchall()
            
        recommend_data = list(row)
        #recommend_data = readingFile(sys.argv[1])
        #crossValidation(recommend_data)
        print("recommend_data",recommend_data)
        ddd = predictRating(recommend_data)

        userid = c - 1
        print(userid)        
        print("BBBBBB",ddd[userid])
        flval = format(ddd[userid], ".1f")
        print("BBBBBB",type(flval))
        
        df = pd.DataFrame(p, columns = ['a', 'b','c', 'd','e', 'f','g', 'h','i'])
        dfk1=df[df["d"]==float(flval)]
        dfk2=df[df["d"]!=float(flval)]
        dfk2 = dfk2.sort_values(by=['d'], ascending=False)
        frames2=[dfk1,dfk2]
        finaldf = pd.concat(frames2)  
        
        finallist = finaldf.values.tolist()
        
        jsonObj = json.dumps(finallist)     
        
        return jsonObj
    
@app.route('/getRestaurantData', methods=['GET', 'POST'])
def getRestaurantData():
    if request.method == 'POST':
        
        username = request.form.get("username")
        print("I am in Restaurant")
                
        cursor.execute('SELECT area FROM restaurant_db')
        row = cursor.fetchall()
        
        flat_list = []
        for sublist in row:
            for item in sublist:
                flat_list.append(item)
                
        myList = getTSPOutput(flat_list) 
        
        p=list() 
        for i in myList:
            # print(flat_list[i])
            cursor.execute('SELECT * FROM restaurant_db WHERE area = %s', (flat_list[i]))
            row = cursor.fetchall()
            a=row[0]
            p.append(a)
        print(p)
        
        cursor.execute('SELECT id FROM usertable WHERE username = %s',(username))
        row = cursor.fetchall()
        c = int(row[0][0])

        print("row",row)

        # re_list=list()
        cursor.execute('SELECT * FROM recomm')
        row = cursor.fetchall()
            
        recommend_data = list(row)
        #recommend_data = readingFile(sys.argv[1])
        #crossValidation(recommend_data)
        print("recommend_data",recommend_data)
        ddd = predictRating(recommend_data)

        userid = c - 1
        print(userid)        
        print("BBBBBB",ddd[userid])
        flval = format(ddd[userid], ".1f")
        print("BBBBBB",type(flval))
        
        df = pd.DataFrame(p, columns = ['a', 'b','c', 'd','e', 'f','g', 'h','i','j'])
        dfk1=df[df["d"]==float(flval)]
        dfk2=df[df["d"]!=float(flval)]
        dfk2 = dfk2.sort_values(by=['d'], ascending=False)
        frames2=[dfk1,dfk2]
        finaldf = pd.concat(frames2)  
        
        finallist = finaldf.values.tolist()
        
        jsonObj = json.dumps(finallist) 
        
        return jsonObj
    
@app.route('/getRecreationData', methods=['GET', 'POST'])
def getRecreationData():
    if request.method == 'POST':
        
        username = request.form.get("username")
        print("I am in Recreation")
                
        cursor.execute('SELECT area FROM recreation_db')
        row = cursor.fetchall()
        
        flat_list = []
        for sublist in row:
            for item in sublist:
                flat_list.append(item)
                
        myList = getTSPOutput(flat_list) 
        
        p=list() 
        for i in myList:
            # print(flat_list[i])
            cursor.execute('SELECT * FROM recreation_db WHERE area = %s', (flat_list[i]))
            row = cursor.fetchall()
            a=row[0]
            p.append(a)
        print(p)

        cursor.execute('SELECT id FROM usertable WHERE username = %s',(username))
        row = cursor.fetchall()
        c = int(row[0][0])

        print("row",row)

        # re_list=list()
        cursor.execute('SELECT * FROM recomm')
        row = cursor.fetchall()
            
        recommend_data = list(row)
        #recommend_data = readingFile(sys.argv[1])
        #crossValidation(recommend_data)
        print("recommend_data",recommend_data)
        ddd = predictRating(recommend_data)

        userid = c - 1
        print(userid)        
        print("BBBBBB",ddd[userid])
        flval = format(ddd[userid], ".1f")
        print("BBBBBB",type(flval))
        
        df = pd.DataFrame(p, columns = ['a', 'b','c', 'd','e', 'f','g', 'h','i','k'])
        dfk1=df[df["d"]==float(flval)]
        dfk2=df[df["d"]!=float(flval)]
        dfk2 = dfk2.sort_values(by=['d'], ascending=False)
        frames2=[dfk1,dfk2]
        finaldf = pd.concat(frames2)  
        
        
        finallist = finaldf.values.tolist()
        
        jsonObj = json.dumps(finallist) 
        
        return jsonObj
    

"---------------------------------------------------------------------------------------"
        
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

dist_matrix = np.asarray(dist_matrix)

for i in range(0, len(places), 1):
    for j in range(i+1, len(places), 1):
        dist_matrix[j,i] = dist_matrix[i,j]
dist_matrix = np.asarray(dist_matrix)

# print(dist_matrix)

"""Entry point of the program."""
# Instantiate the data problem.
data = create_data_model(dist_matrix,places)

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

"---------------------------------------------------------------------------------------"

# cursor.execute('SELECT id FROM usertable WHERE username = %s',("a"))
# row = cursor.fetchall()
# c = int(row[0][0])

# print("row",row)

# re_list=list()
# cursor.execute('SELECT * FROM recomm')
# row = cursor.fetchall()
    
# recommend_data = list(row)
# #recommend_data = readingFile(sys.argv[1])
# #crossValidation(recommend_data)
# print("recommend_data",recommend_data)
# ddd = predictRating(recommend_data)


# userid = c - 1
# print(userid)
# print("BBBBBB",ddd[userid])

# cursor.execute('SELECT area FROM place_db WHERE rating >= %s',(ddd[userid]))
# # cursor.execute('SELECT area FROM hotel_db')
# row = cursor.fetchall()
# print("BBBBBB",row)

# cursor.execute('SELECT area FROM place_db')
# row = cursor.fetchall()
# print("row",row)

cursor.execute('SELECT id FROM usertable WHERE username = %s',("a"))
row = cursor.fetchall()
c = int(row[0][0])

print("row",row)

re_list=list()
cursor.execute('SELECT * FROM recomm')
row = cursor.fetchall()
    
recommend_data = list(row)
#recommend_data = readingFile(sys.argv[1])
#crossValidation(recommend_data)
print("recommend_data",recommend_data)
ddd = predictRating(recommend_data)

userid = c - 1
print(userid)
print("BBBBBB",type(ddd[userid]))

cursor.execute('SELECT area FROM hotel_db WHERE rating >= %s',(ddd[userid]))
# cursor.execute('SELECT area FROM hotel_db')
row = cursor.fetchall()
print("BBBBBB",row)


"----------------------------------------------------------------------------------------------"


    
if __name__ == "__main__":
    app.run("0.0.0.0")
    # getRestaurantData()