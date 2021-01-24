import math
import numpy as np
import random as rm

#Defining the vertexes for the transition matrix and the proportionality constant k
points = ["000","001","010","011","100","101","110","111"]

k = 6/(18+9*(math.sqrt(2))+2*(math.sqrt(3)))

#Defining possible transitions
transition_code = [["000000","000001","000010","000011","000100","000101","000110","000111"],
                  ["001000","001001","001010","001011","001100","001101","001110","001111"],
                  ["010000","010001","010010","010011","010100","010101","010110","010111"],
                  ["011000","011001","011010","011011","011100","011101","011110","011111"],
                  ["100000","100001","100010","100011","100100","100101","100110","100111"],
                  ["101000","101001","101010","101011","101100","101101","101110","101111"],
                  ["110000","110001","110010","110011","110100","110101","110110","110111"],
                  ["111000","111001","111010","111011","111100","111101","111110","111111"]]
                  
                  #Filling the matrix with probabilities
transition_matrix =[[0,k,k,k/math.sqrt(2),k,k/math.sqrt(2),k/math.sqrt(2),k/math.sqrt(3)],
                    [k,0,k/math.sqrt(2),k,k/math.sqrt(2),k,k/math.sqrt(3),k/math.sqrt(2)],
                    [k,k/math.sqrt(2),0,k,k/math.sqrt(2),k/math.sqrt(3),k,k/math.sqrt(2)],
                    [k/math.sqrt(2),k,k,0,k/math.sqrt(3),k/math.sqrt(2),k/math.sqrt(2),k],
                    [k,k/math.sqrt(2),k/math.sqrt(2),k/math.sqrt(3),0,k,k,k/math.sqrt(2)],
                    [k/math.sqrt(2),k,k/math.sqrt(3),k/math.sqrt(2),k,0,k/math.sqrt(2),k],
                    [k/math.sqrt(2),k/math.sqrt(3),k,k/math.sqrt(2),k,k/math.sqrt(2),0,k],
                    [k/math.sqrt(3),k/math.sqrt(2),k/math.sqrt(2),k,k/math.sqrt(2),k,k,0]]

transition_matrix = np.array(transition_matrix)

#Forecasting the probability of having landed on vertex "111" after s steps

def Markov_forecast (steps):
    current_points = [1,0,0,0,0,0,0,0]
    i=0
    #prob = 0
    while i != steps+1:
        #total_points is the new distribution ignoring absorption 
        total_points = np.array(np.dot(current_points,transition_matrix))
        #absorbing_point is the probability of going from "111" to other points
        absorbing_point = (current_points[7]*transition_matrix[7,:])
        #current_points is the adjusted distribition
        current_points = np.subtract(total_points, absorbing_point)
        current_points[7]=(1-sum(current_points))
       
        prob = current_points[7]
        i += 1
        
    return prob, current_points
            

#Absorbing Markov chain
absorbing_Markov =[[0,k,k,k/math.sqrt(2),k,k/math.sqrt(2),k/math.sqrt(2),k/math.sqrt(3)],
                    [k,0,k/math.sqrt(2),k,k/math.sqrt(2),k,k/math.sqrt(3),k/math.sqrt(2)],
                    [k,k/math.sqrt(2),0,k,k/math.sqrt(2),k/math.sqrt(3),k,k/math.sqrt(2)],
                    [k/math.sqrt(2),k,k,0,k/math.sqrt(3),k/math.sqrt(2),k/math.sqrt(2),k],
                    [k,k/math.sqrt(2),k/math.sqrt(2),k/math.sqrt(3),0,k,k,k/math.sqrt(2)],
                    [k/math.sqrt(2),k,k/math.sqrt(3),k/math.sqrt(2),k,0,k/math.sqrt(2),k],
                    [k/math.sqrt(2),k/math.sqrt(3),k,k/math.sqrt(2),k,k/math.sqrt(2),0,k],
                    [0,0,0,0,0,0,0,1]]
                    

def Markov_absorption (steps):
    current_points = [1,0,0,0,0,0,0,0]
    i=0
    
    while i != steps:
        current_points = np.dot(current_points,absorbing_Markov)
        i += 1
        
    return current_points
    
Markov_absorption(4)