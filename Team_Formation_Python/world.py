import sys
sys.path.insert(0, r'C:\Users\manas\Documents\Codes\BioAI\Final')
import numpy as np
import random
import brain
import time
import matplotlib.pyplot as plt

class world:
    def __init__(self):
        self.grid_x = 3
        self.grid_y = 3
        self.grid_length = self.grid_x * self.grid_y
        self.grid_dict = {}
        self.team_size = 3
        self.no_of_teams = 3
        self.pop = self.team_size * self.no_of_teams
        self.agent_states = [-1 for x in range(self.pop)]
        self.actions = {'up': (-1 * self.grid_x), 'left': (-1), 'right': (+1), 'down': (+1 * self.grid_x) ,'stay':(0)}
        self.agents = [brain.brain(self.grid_dict,self.grid_length, self.team_size, self.actions, self.agent_states, self.grid_x, self.grid_y) for x in range(self.pop)]

    def initialize_grid(self):
        for i in range(self.grid_y):
            for j in range(self.grid_x):
                self.grid_dict[self.grid_x * i + j] = []


    def populate_world(self):
        sample_list = []
        for i in range(self.grid_length):
            for j in range(self.team_size):
                sample_list.append(i)



        self.agent_states = random.sample(sample_list, self.pop)
        for i in range(len(self.agent_states)):
            self.grid_dict[self.agent_states[i]].append(i % self.no_of_teams)

    def step(self,old_dict,i):
        friendlies = old_dict[self.agent_states[i]].count(i % self.team_size)
        enemies = len(old_dict[self.agent_states[i]]) - friendlies
        self.agents[i].grid_reward[self.agent_states[i]] += self.agents[i].reward_gate([enemies, friendlies, i % self.team_size])
        act = self.agents[i].get_action(self.agent_states[i])
        self.agent_states[i] = self.agent_states[i] + self.actions[act]
        self.grid_dict[self.agent_states[i]].append(i % self.no_of_teams)
        self.agents[i].grid_dict = self.grid_dict


    def update_step(self):
        old_dict = self.grid_dict
        self.initialize_grid()
        for i in range(self.pop):
            self.step(old_dict,i)
            # if len(self.grid_dict[self.agent_states[i]]) > self.team_size:
            #     self.step(self.grid_dict,i)



    def view_grid(self,epi):
         
        color = ['b','g','r','c','m','y','k','w']
        plt.xlim([0,self.grid_x])
        plt.ylim([0,self.grid_y])
        plt.xticks(range(0, self.grid_x))
        plt.yticks(range(0, self.grid_y))
        plt.rc('grid', linestyle="-")
        plt.grid(True)
        plt.title('Episode: '+ str(epi))
        
        for i,j in self.grid_dict.items():
            y = i % self.grid_y +0.1
            x = (i-y) / self.grid_x +0.1
            for j in range(len(j)):                
                plt.scatter(x, y)
                x = x + 0.1
        fig.canvas.draw()

if __name__ == "__main__":
    print("Training")
    world = world()
    world.initialize_grid()
    world.populate_world()
    episodes = 1000
    episode_length = 10

    fig = plt.gcf()
    fig = plt.figure()
    fig.show()
    fig.canvas.draw()
    fig.clf()
        
    for j in range(episodes):
        world.initialize_grid()
        world.populate_world()
        for i in range(episode_length):
            print(world.grid_dict)
            print("epi - " + str(j))
            print("step - " + str(i))
            world.update_step()
        world.view_grid(j)
        time.sleep(2)
        fig.clf()
        
