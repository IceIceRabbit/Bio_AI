#the GA

import math
import random
import numpy as np
import time
import brain
import world


class GA:

    def __init__(self, Pc):

        self.r = 1                                          #number of parents
        self.m = 5                                          #number of individuals/actions
        self.Pc = Pc                                        #probability of crossover
        self.Pm = 1-Pc                                      #probability of mutation

        self.fitz = []                                      #list of fitnesses of the individuals
        #self.fitz = brain.surrounding_rewards()
        self.Rp = 0                                         #parent
        self.M_now = world.action()                         #stop, up, down, right, left action population
        self.fin_act = 0
    """
    Arguments in functions
    Tot = list of total population
    Par = list of parents
    t = number of individuals in the population
    p = number of parents
    ps = list of probability of selection of individuals in the population
    acti = action to take
    """


    def nearz(self, q, arr):                                                        #calculates the nearest element in the array (arr) to the number q
        minz = np.amax(arr)
        arr = arr.tolist()
        return arr.index(minz)




    def fitness(self, fit):                                                         #CODE TESTING ONLY
         fit.append(0)
         fit.append(-1)
         fit.append(-1)
         fit.append(-1)
         fit.append(5)
 #        fit = brain.surrounding_rewards()                                          #array of fitnesss of all individuals GET FROM BRAIN



    def delete_walls(self): 
        for i in range(len(self.M_now)-1, 0, -1):
            if self.fitz[i] == -1:
                del self.fitz[i]
                del self.M_now[i]

            


    def selection(self, Tot, fit):                                       #select BEST, aka direction with highest fitness
        maxi = self.nearz(50,np.array(fit))
        self.Rp = Tot[maxi]



    def clutate(self):                                                        #clone OR mutate
        
        rand0 = random.random()                                               #select random number between 0-1 to compare to crossover/cloning probability
        if rand0 < self.Pc:
            print("Cloned")
            self.fin_act = self.M_now.index(self.Rp)
        else:                                                                 #else mutate
            self.fin_act = random.randrange(0,len(self.M_now)-1)
            print("Mutated")



    def get_action(self):
        self.fitness(self.fitz)
        print("[stay(0), up(1), down(2), right(3), left(4)]")
        print("Fitnesses: " + str(self.fitz))
        print("Actions: " + str(self.M_now))
        self.selection(self.M_now, self.fitz)
        self.clutate()
        return self.fin_act


for x in range(30):                                                           #run for 30 GENS
    gee = GA(0.5)
    flee = gee.get_action()
    if gee.M_now[flee] == 0:
        print("stay")
    elif gee.M_now[flee] == 1:
        print("up")
    elif gee.M_now[flee] == 2:
        print("down")
    elif gee.M_now[flee] == 3:
        print("right")
    elif gee.M_now[flee] == 4:
        print("left")
