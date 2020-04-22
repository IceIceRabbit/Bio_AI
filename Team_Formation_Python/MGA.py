#the GA

import math
import random
import numpy as np
import time
import brain
import world


class GA:

    def __init__(self):

        self.r = 1                                          #number of parents
        self.m = 5                                          #number of individuals/actions
        self.Pc = 0                                        #probability of crossover

        self.fitz = []                                      #list of fitnesses of the individuals
        self.Rp = 0                                         #parent
        self.M_now = ["stay", "up", "down", "right", "left"]                        #stop, up, down, right, left action population
        self.fin_act = 0


    def fitness(self, state):
        here = state
        up = state - world.grid_length
        down = state + world.grid_length
        right = state + 1
        left = state - 1
        fitness = [.grid_reward(here), world.grid_reward(up),
                   world.grid_reward(down), world.grid_reward(right),
                   world.grid_reward(left)]
        self.fitz = fitness

        


    def delete_walls(self, agent):
        
        for i in range(len(self.M_now)-1, 1, -1):
            act = M_now[i]
            action_check = world.actions[act]
            fut_state = world.agent_states[agent] + world.actions[act]
            if action_check == 1 or -1:
                if action_check == 1 and fut_state % world.grid_x == 0:
                    del self.fitz[i]
                    del self.M_now[i]
                elif action_check == -1 and fut_state % world.grid_y == world.grid_x - 1:
                    del self.fitz[i]
                    del self.M_now[i]
            elif fut_state > 0 or fut_state < world.grid_length:
                    del self.fitz[i]
                    del self.M_now[i]


    def selection(self):                                                      #select BEST, aka direction with highest fitness
        
        maxi = np.amax(np.array(self.fitz))
        self.fitz = maxi.tolist()
        self.Rp = self.M_now[self.fitz.index(maxi)]



    def clutate(self):                                                        #clone OR mutate
        
        rand0 = random.random()                                               #select random number between 0-1 to compare to crossover/cloning probability
        if rand0 < self.Pc:
            print("Cloned")
            self.fin_act = self.M_now.index(self.Rp)
        else:                                                                 #else mutate
            self.fin_act = random.randrange(0,len(self.M_now)-1)
            print("Mutated")



    def get_action(self, Pc, state):

        self.fitness(state)
        self.Pc = Pc
        self.delete_walls(state)
        print("Fitnesses: " + str(self.fitz))
        print("Actions: " + str(self.M_now))
        self.selection()
        self.clutate()
        return self.fin_act


