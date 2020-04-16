#the GA

###########################################  PACKAGES      ##########################################################################
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import time


############################################   FUNCTIONS    ##########################################################################3
##Arguments in functions
##Tot = list of total population
##Par = list of parents
##t = number of individuals in the population
##p = number of parents
##ps = list of probability of selection of individuals in the population


def funktion(m):                                               #arg: individual from the population
    return ("obtain possible fitness function from nodes"
            "and return an array of 5 fitness values per organism")      #returns the function value for that argument


def nearz(q, arr):                                             #calculates the nearest element in the array (arr) to the number q
    arr = abs(arr-q)
    minz = np.amin(arr)
    arr = arr.tolist()
    return arr.index(minz)




"""
calculate 4 fitness values for every organism
"""
def fitness(Tot, t, fit):
    for j in range (0,t):                                               #array of fitnesss of all individuals
        fit.append(funktion(float(Tot[j])))


"""
take avg from every array corresponding
to each organism
"""
def selection_prob(Tot, t, fit, ps):
    for k in range(0,t):                                                #computing probability of individuals being selected
        ps.append(funktion(Tot[k]) / sum(fit))                          


"""
Select from array of possible directions
for every organism
"""
def selection(Tot, Par, t, p, ps):
    for l in range (0,p):                                               #selecting parents from the population
        el = random.randrange(0,t)                                      #roulette style parent selection
        rand = random.random()                                          #generate a random number to compare with
        if rand < sum(ps[j] for j in range(0,el)):                      #if randomly chosen probability is less than selection probability of randomly chosen parent
            Par.append(Tot[el])                                         #select parent selected in roulette
        else:                                                           #select parent whose selection probability correspods closest to the random probability
            mini = nearz(rand,np.array(ps))
            Par.append(Tot[mini])


"""
clone the randomly chosen parent
"""
def crossover(Tot, Par, t, p):
    for j in range(0,t-p):
        rand0 = random.random()                                               #select random number between 0-1 to compare to crossover probability
        rand1 = random.randrange(0,p)                                         #randomly select one parent to clone
        Tot.append(str(rand1))

"""
mutate the obtained value if GA is apled to all MBs
or dynamically change mutation and crossover probabilities
"""
def mutat(Tot, t, p):
    
    for j in range(0,t-p):
        if random.random() < Pm:
            m = Tot[j]
            
            m = list(str(m))
            r = random.randrange(0,5)                                        #generating random mutating number
            rand = list(str(r))
            randy = random.randrange(0,len(m))                               #only mutate after decimal point (only parameters and not the point itself)
            
            m[randy] = rand[0]
            Tot[j] = int(m)
            
        
def rand_gen():                                             #function to randomly generate values between -0.5 and 1
    for i in range(0,m):
        em.append(round((random.uniform(-0.5,1)),v))        #decimal points (genes)

####################################################   FUNCTIONS END     ###########################################################


####################################################  GLOBAL VARIABLES   ###########################################################
v = 1                                          #number of parameters
r = 3                                          #number of parents
m = 16                                         #number of individuals
Pc = 1                                         #probability of crossover
Pm = 0.5                                       #probability of mutation

em = []                                        #population
#rand_gen()


fitz = []                                      #list of fitnesses of the individuals
Rp = []                                        #list of parents
Ps = []                                        #list of selection probabilities of individuals
i = 1                                          #Generation number
M_next = em

v = v+3


#################################################     GLOBAL VARIABLES END         ##################################################

#################################################      MAIN PROGRAM                ##################################################

while (sum(fitz))/m < "add fitness" and i<=50:            #termination criteria: stops if average fitness is greater than "addfitness" or 50 generations, whichever comes first


    M_now = M_next                               #update current generation with new population
  
    Rp = []                                      #clearing old parents, fitnesses and selection probabilities
    fitz = []
    Ps = []

    fitness(M_now, m, fitz)
    selection_prob(M_now, m, fitz, Ps)
    b = fitz[nearz(2,np.array(fitz))]
    w = fitz[nearz(0,np.array(fitz))]
    avg = (sum(fitz))/m
    ind = M_now[nearz(2,np.array(fitz))]

    
    selection(M_now, Rp, m, r, Ps)
    M_now = []

    
    M_next = Rp
    crossover(M_next, Rp, m, r)
    mutat(M_next, m, r)
    
    print()
    print()
    i+=1
print("Done")

####################################################   END OF PROGRAM     ###########################################################
