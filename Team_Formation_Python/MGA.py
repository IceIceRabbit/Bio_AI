import sys
sys.path.insert(0, r'C:\Users\manas\Documents\Codes\BioAI\Final')
import math
import random
import numpy as np
import time



class MGA:

    def __init__(self, grid_length, grid_reward, actions, agent_states, grid_x, grid_y):

        self.r = 1                                          #number of parents
        self.m = 5                                          #number of individuals/actions
        self.Pc = 0                                         #probability of crossover

        self.fitz = []                                      #list of fitnesses of the individuals
        self.Rp = 0                                         #parent
        self.M_now = ["up", "down", "right", "left"]                        #stop, up, down, right, left action population
        self.fin_act = 0
        self.grid_length = grid_length
        self.grid_reward = grid_reward
        self.actions = actions
        self.agent_states = agent_states
        self.grid_x = grid_x
        self.grid_y = grid_y


    def fitness(self, tot, state):
        fit = []
        for j in range(len(tot)):
            i = tot[j]
            fit.append(self.grid_reward[state + self.actions[i]])
            print(fit)
        self.fitz = fit
        

        


    def delete_walls(self, agent):
        
        for i in range(len(self.M_now)-1, -1, -1):
            act = self.M_now[i]
            action_check = self.actions[act]
            fut_state = agent + self.actions[act]
            if action_check == 1 or action_check == -1:
                if action_check == 1 and fut_state % self.grid_x == 0:
                    del self.M_now[i]
                elif action_check == -1 and fut_state % self.grid_y == self.grid_x - 1:
                    del self.M_now[i]
            elif fut_state < 0 or fut_state >= self.grid_length:
                    del self.M_now[i]


    def selection(self):                                                      #select BEST, aka direction with highest fitness
        
        maxi = np.amax(np.array(self.fitz))
        self.Rp = self.M_now[self.fitz.index(maxi)]



    def clutate(self):                                                        #clone OR mutate
        
        rand0 = random.random()                                               #select random number between 0-1 to compare to crossover/cloning probability
        if rand0 < self.Pc:
            #print("Cloned")
            self.fin_act = self.M_now.index(self.Rp)
        else:                                                                 #else mutate
            self.fin_act = random.randrange(0,len(self.M_now)-1)
            #print("Mutated")



    def move(self, Pc, state):

        
        self.Pc = Pc
        self.delete_walls(state)
        self.fitness(self.M_now, state)
        self.selection()
        self.clutate()
        return self.M_now[self.fin_act]
