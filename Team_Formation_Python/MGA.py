import sys
sys.path.insert(0, r'C:\Users\manas\Documents\Codes\BioAI\Final')
import math
import random
import numpy as np
import time
import copy



class MGA:

    def __init__(self,grid_dict, grid_length, grid_reward, actions, agent_states, grid_x, grid_y,team_size):

        self.r = 1                                          #number of parents
        self.m = 5                                          #number of individuals/actions
        self.Pc = 0                                         #probability of crossover

        self.fitz = []                                      #list of fitnesses of the individuals
        self.Rp = 0                                         #parent
        self.M_now = ["up", "down", "right", "left","stay"
                      ]                        #stop, up, down, right, left action population
        self.fin_act = 0
        self.grid_dict = grid_dict
        self.grid_length = grid_length
        self.grid_reward = grid_reward
        self.actions = actions
        self.agent_states = agent_states
        self.team_size = team_size
        self.grid_x = grid_x
        self.grid_y = grid_y


    def fitness(self, tot, state):
        fit = []
        for j in range(len(tot)):
            i = tot[j]
            fit.append(self.grid_reward[state + self.actions[i]])
            # print(fit)
        self.fitz = fit
        

        


    def delete_walls(self, agent):
        possible_states = copy.copy(self.M_now)
        # print(self.M_now)
        for i in range(len(self.M_now)-1, -1, -1):
            act = possible_states[i]
            action_check = self.actions[act]
            fut_state = agent + self.actions[act]
            if action_check == 1 or action_check == -1:
                if action_check == 1 and fut_state % self.grid_x == 0:
                    del possible_states[i]
                elif action_check == -1 and fut_state % self.grid_y == self.grid_x - 1:
                    del possible_states[i]
            elif fut_state < 0 or fut_state >= self.grid_length:
                    del possible_states[i]
            elif len(self.grid_dict.get(fut_state)) >= self.team_size:
                del possible_states[i]

        return possible_states


    def selection(self,actions):                                                      #select BEST, aka direction with highest fitness
        
        maxi = np.amax(np.array(self.fitz))
        self.Rp = actions[self.fitz.index(maxi)]



    def clutate(self,possible_acts):                                                        #clone OR mutate
        
        rand0 = random.random()                                               #select random number between 0-1 to compare to crossover/cloning probability
        # print(self.M_now)
        if rand0 < self.Pc:
            #print("Cloned")
            self.fin_act = possible_acts.index(self.Rp)
        else:                                                                 #else mutate
            self.fin_act = random.randint(0,len(possible_acts) - 1)
            #print("Mutated")



    def move(self, Pc, state):

        
        self.Pc = Pc
        pos_actions = self.delete_walls(state)
        self.fitness(pos_actions, state)
        self.selection(pos_actions)
        self.clutate(pos_actions)
        return pos_actions[self.fin_act]
