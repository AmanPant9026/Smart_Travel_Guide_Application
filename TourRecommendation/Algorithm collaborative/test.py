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
#from sklearn.utils.extmath import np.dot
from scipy.spatial import distance
warnings.simplefilter("error")

users = 4
items = 5
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
                for i in range (0,n):  #looping through each element of the list
                    difference = y[i] - y_bar[i]  #finding the difference between observed and predicted value
                    squared_difference = difference**2  #taking square of the differene 
                    summation = summation + squared_difference  #taking a sum of all the differences
                MSE = summation/n  #dividing summation by total values to obtain average
                print("The Mean Square Error is: " , MSE)
                dst = distance.euclidean(y, y_bar)
                print("dst is: " , dst)
                by_algo_prediction[user1][user2]=dst
               
                try:
                    if not math.isnan(scipy.stats.pearsonr(data[item1],data[item2])[0]):
                        item_similarity_pearson[item1][item2] = scipy.stats.pearsonr(data[item1],data[item2])[0]
                    else:
                        item_similarity_pearson[item1][item2] = 0
                except:
                    item_similarity_pearson[item1][item2] = 0

            #f_i_d.write(str(item1) + "," + str(item2) + "," + str(item_similarity_cosine[item1][item2]) + "," + str(item_similarity_jaccard[item1][item2]) + "," + str(item_similarity_pearson[item1][item2]) + "\n")
    #f_i_d.close()
    return item_similarity_cosine, item_similarity_jaccard, item_similarity_pearson


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
                for i in range (0,n):  #looping through each element of the list
                    difference = y[i] - y_bar[i]  #finding the difference between observed and predicted value
                    squared_difference = difference**2  #taking square of the differene 
                    summation = summation + squared_difference  #taking a sum of all the differences
                MSE = summation/n  #dividing summation by total values to obtain average
                print("The Mean Square Error is: " , MSE)
                dst = distance.euclidean(y, y_bar)
                print("dst is: " , dst)
                by_algo_prediction[user1][user2]=dst
                
                
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

recommend_data = readingFile("test.csv")
print(recommend_data)
similarity_user(recommend_data)
