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

prob_dict = []

for linha_code, linha_matrix in zip(transition_code, transition_matrix):
    nova_linha = {}
    for e_code, e_matrix in zip(linha_code, linha_matrix):
         nova_linha[e_code] = e_matrix
    prob_dict.append(nova_linha)

#print(prob_dict)

#transition_matrix = np.array(transition_matrix)

def find_line(point, prob_dict):
    for line in prob_dict:
        for e in line:
            if (e[:3] == point):
                return prob_dict.index(line)


def calculate(n, final_point, prob_dict):
    list_steps = []
    current_point = "000"
    for _ in range(0, n):
        steps = 0
        line = 0
        while(True):
            current_point = np.random.choice(list(prob_dict[line].keys()), 1, p=list(prob_dict[line].values()))[0][3:]
            if (current_point == final_point):
                list_steps.append(steps)
                break
            line = find_line(current_point, prob_dict)
            steps+=1


    avg_steps = sum(list_steps)/len(list_steps)

    return list_steps, avg_steps


print(calculate(1000000, "111", prob_dict)[1])

#print(prob_dict[0].values())