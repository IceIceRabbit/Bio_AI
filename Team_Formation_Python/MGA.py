#the GA

###########################################  PACKAGES      ##########################################################################
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import time



class GA:

    def __init__(self, Pc):

        self.r = 1                                          #number of parents
        self.m = 5                                          #number of individuals/actions
        self.Pc = Pc                                        #probability of crossover
        self.Pm = 1-Pc                                      #probability of mutation

        self.fitz = []                                      #list of fitnesses of the individuals
        self.Rp = 0                                         #parent
        self.M_now = [0, 1, 2, 3, 4]                        #stop, up, down, right, left action population
        
    """
    Arguments in functions
    Tot = list of total population
    Par = list of parents
    t = number of individuals in the population
    p = number of parents
    ps = list of probability of selection of individuals in the population
    acti = action to take
    """

    def funktion(self, m):                                                          #arg: individual from the population
        return ("call brain function")                                              #returns the function value for that argument


    def nearz(self, q, arr):                                                        #calculates the nearest element in the array (arr) to the number q
        arr = abs(arr-q)
        minz = np.amin(arr)
        arr = arr.tolist()
        return arr.index(minz)




    def fitness(self, Tot, t, fit):
        for j in range (0,t):                                                 #array of fitnesss of all individuals
            fit.append(self.funktion(float(Tot[j])))



    def selection(self, Tot, fit, Par):                                       #select BEST, aka direction with highest fitness
        maxi = self.nearz(50,np.array(fit))
        Par = Tot[mini]



    def clutate(self, acti, Pc):                                              #clone OR mutate
        
        rand0 = random.random()                                               #select random number between 0-1 to compare to crossover/cloning probability
        if rand0 > self.Pc:
            acti = rand1
        else:                                                                 #else mutate
            acti = random.randrange(0,5)



    def run():
            self.fitness(self.M_now, self.m, self.fitz)

            self.selection(self.M_now, self.fitz, self.Rp)

            self.clutate(fin_act, self.Pc)
            print(fin_act)
            return fin_act


