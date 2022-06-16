# -*- coding: utf-8 -*-
"""
Created on Sat May  1 17:34:26 2021

@author: INBOTICS
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 15:39:13 2021

@author: INBOTICS
"""
import numpy as np
import scipy.stats
import scipy.spatial
from sklearn.model_selection import KFold
import random
from sklearn.metrics import mean_squared_error
from math import sqrt
import math
import warnings
import sys
from math import sqrt
#from sklearn.utils.extmath import np.dot
from scipy.spatial import distance
warnings.simplefilter("error")

users = 6040
items = 3952
X=np.arange(0,6)
def readingFile(filename):
    f = open(filename,"r")
    data = []
    for row in f:
        r = row.split(',')
        e = [int(r[0]), int(r[1]), int(r[2])]
        data.append(e)
    return data
def similarity_item(data):
    print("Hello Item")
    #f_i_d = open("sim_item_hybrid.txt","w")
    item_similarity_cosine = np.zeros((items,items))
    item_similarity_jaccard = np.zeros((items,items))
    item_similarity_pearson = np.zeros((items,items))
    by_algo_prediction=np.zeros((items,items))
    for item1 in range(items):
        print (item1)
        for item2 in range(items):
            if np.count_nonzero(data[item1]) and np.count_nonzero(data[item2]):
                item_similarity_cosine[item1][item2] = 1-scipy.spatial.distance.cosine(data[item1],data[item2])
                item_similarity_jaccard[item1][item2] = 1-scipy.spatial.distance.jaccard(data[item1],data[item2])
                y=data[item1]
                summation = 0
                print('check1')
                y_bar=data[item2]
                print('check11',y_bar,'second is',y)
                #if y!=y_bar:
                print('check2')
                n = len(y) #finding total number of items in list
                MSElist=[]
                
                for i in range (0,n):  #looping through each element of the list
                    difference = y[i] - y_bar[i]  #finding the difference between observed and predicted value
                    squared_difference = difference**2  #taking square of the differene 
                    summation = summation + squared_difference  #taking a sum of all the differences
                    MSElist.append(squared_difference+1)
                MSE = summation/n  #dividing summation by total values to obtain average
                
                MSEdr=n*max(MSElist)
                MSEall=MSE/MSEdr
                
                print("The Mean Square Error is: " , MSE)
                print("The Mean Square Error MSEall: " , MSEall)
                dst = distance.euclidean(y, y_bar)
                print("dst is: " , dst)
                if dst>2000 and MSE >15000 and MSEall>0.12 :
                    by_algo_prediction[item1][item2]=0.45
                else:
                    by_algo_prediction[item1][item2]=1
                    
               
                try:
                    if not math.isnan(scipy.stats.pearsonr(data[item1],data[item2])[0]):
                        item_similarity_pearson[item1][item2] = scipy.stats.pearsonr(data[item1],data[item2])[0]
                    else:
                        item_similarity_pearson[item1][item2] = 0
                except:
                    item_similarity_pearson[item1][item2] = 0

            #f_i_d.write(str(item1) + "," + str(item2) + "," + str(item_similarity_cosine[item1][item2]) + "," + str(item_similarity_jaccard[item1][item2]) + "," + str(item_similarity_pearson[item1][item2]) + "\n")
    #f_i_d.close()
    return item_similarity_cosine, item_similarity_jaccard, item_similarity_pearson,by_algo_prediction


def similarity_user(data):
    print ("Hello User 1")
    #f_i_d = open("sim_user_based.txt","w")
    user_similarity_cosine = np.zeros((users,users))
    user_similarity_jaccard = np.zeros((users,users))
    user_similarity_pearson = np.zeros((users,users))
    by_algo_prediction= np.zeros((users,users))
    for user1 in range(users):
        print (user1)
        for user2 in range(users):
            if np.count_nonzero(data[user1]) and np.count_nonzero(data[user2]):
                user_similarity_cosine[user1][user2] = 1-scipy.spatial.distance.cosine(data[user1],data[user2])
                user_similarity_jaccard[user1][user2] = 1-scipy.spatial.distance.jaccard(data[user1],data[user2])
                
                
                y=data[user1]
                summation = 0
                print('check1')
                y_bar=data[user2]
                print('check11',y_bar,'second is',y)
                #if y!=y_bar:
                print('check2')
                n = len(y) #finding total number of items in list
                MSElist=[]
                for i in range (0,n):  #looping through each element of the list
                    difference = y[i] - y_bar[i]  #finding the difference between observed and predicted value
                    squared_difference = difference**2  #taking square of the differene 
                    summation = summation + squared_difference  #taking a sum of all the differences
                    MSElist.append(squared_difference+1)
                MSE = summation/n  #dividing summation by total values to obtain average
                
                MSEdr=n*max(MSElist)
                MSEall=MSE/MSEdr
                
                print("The Mean Square Error is: " , MSE)
                print("The Mean Square Error MSEall: " , MSEall)
                dst = distance.euclidean(y, y_bar)
                print("dst is: " , dst)
                if dst>2000 and MSE >15000 and MSEall>0.12:
                    by_algo_prediction[user1][user2]=0.45
                else:
                    by_algo_prediction[user1][user2]=1
                try:
                    if not math.isnan(scipy.stats.pearsonr(data[user1],data[user2])[0]):
                        user_similarity_pearson[user1][user2] = scipy.stats.pearsonr(data[user1],data[user2])[0]
                    else:
                        user_similarity_pearson[user1][user2] = 0
                except:
                    user_similarity_pearson[user1][user2] = 0

            #f_i_d.write(str(user1) + "," + str(user2) + "," + str(user_similarity_cosine[user1][user2]) + "," + str(user_similarity_jaccard[user1][user2]) + "," + str(user_similarity_pearson[user1][user2]) + "\n")
    #f_i_d.close()
    print(user_similarity_cosine, user_similarity_jaccard, user_similarity_pearson,by_algo_prediction)
    return user_similarity_cosine, user_similarity_jaccard, user_similarity_pearson,by_algo_prediction

recommend_data = readingFile("ratings.csv")
print(recommend_data)
sim_user_cosine, sim_user_jaccard, sim_user_pearson,by_algo_user=similarity_user(recommend_data)
sim_item_cosine, sim_item_jaccard, sim_item_pearson,by_algo_item=similarity_item(recommend_data)

true_rate = []
actualobtained=[]


for e in recommend_data:
    user = e[0]
    item = e[1]
    #true_rate.append(e[2])

M = np.zeros((users,items))
print(M) 


for e in recommend_data:
	M[e[0]-1][e[1]-1] = e[2]

pred_rate_cosine = []
rmse_cosine=[]  
for e in recommend_data:
    user_pred_cosine = 3.0
    item_pred_cosine = 3.0
    user = e[0]
    item = e[1]
    true_rate.append(e[2])


            #item-based
    if np.count_nonzero(M[:,item-1]):
        sim_cosine = by_algo_item[item-1]
       
        ind = (M[user-1] > 0)
                #ind[item-1] = False
        normal_cosine = np.sum(np.absolute(sim_cosine[ind]))
      
        if normal_cosine > 0:
            item_pred_cosine = np.dot(sim_cosine,M[user-1])/normal_cosine

        if item_pred_cosine < 0:
            item_pred_cosine = 0

        if item_pred_cosine > 5:
            item_pred_cosine = 5


            #user-based
    if np.count_nonzero(M[user-1]):
        sim_cosine = by_algo_user[user-1]
            
        ind = (M[:,item-1] > 0)
                #ind[user-1] = False
        normal_cosine = np.sum(np.absolute(sim_cosine[ind]))
            
        if normal_cosine > 0:
            user_pred_cosine = np.dot(sim_cosine,M[:,item-1])/normal_cosine

            

        if user_pred_cosine < 0:
            user_pred_cosine = 0

        if user_pred_cosine > 5:
            user_pred_cosine = 5


    if (user_pred_cosine != 0 and user_pred_cosine != 5) and (item_pred_cosine != 0 and item_pred_cosine != 5):
        pred_cosine = (user_pred_cosine + item_pred_cosine)/2
    else:
        if (user_pred_cosine == 0 or user_pred_cosine == 5):
            if (item_pred_cosine != 0 and item_pred_cosine != 5):
                pred_cosine = item_pred_cosine
            else:
                pred_cosine = 3.0
        else:
            if (user_pred_cosine != 0 and user_pred_cosine != 5):
                 pred_cosine = user_pred_cosine
            else:
                pred_cosine = 3.0
        
            
            #pred_cosine = (user_pred_cosine + item_pred_cosine)/2
            #pred_jaccard = (user_pred_jaccard + item_pred_jaccard)/2
            #pred_pearson = (user_pred_pearson + item_pred_pearson)/2
    print (str(user) + "\t" + str(item) + "\t" + str(e[2]) + "\t" + str(pred_cosine))
    pred_rate_cosine.append(pred_cosine)
        

        #print len(true_rate)
        #print len(pred_rate_cosine)
    rmse_cosine.append(sqrt(mean_squared_error(true_rate, pred_rate_cosine)))
print(rmse_cosine)

rmse_cosine = sum(rmse_cosine) / float(len(rmse_cosine))
print('avg',rmse_cosine)
