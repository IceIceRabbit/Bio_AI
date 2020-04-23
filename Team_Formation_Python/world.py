import sys
sys.path.insert(0, r'C:\Users\manas\Documents\Codes\BioAI\Final')
import numpy as np
import random
import brain


class world:
    def __init__(self):
        self.grid_x = 3
        self.grid_y = 3
        self.grid_length = self.grid_x * self.grid_y
        self.grid_dict = {}
        self.team_size = 4
        self.no_of_teams = 4
        self.pop = self.team_size * self.no_of_teams
        self.agent_states = [-1 for x in range(self.pop)]
        self.actions = {'up': (-1 * self.grid_x), 'left': (-1), 'right': (+1), 'down': (+1 * self.grid_x)}         
        self.agents = [brain.brain(self.grid_length, self.team_size, self.actions, self.agent_states, self.grid_x, self.grid_y) for x in range(self.pop)]

    def initialize_grid(self):
        for i in range(self.grid_y):
            for j in range(self.grid_x):
                self.grid_dict[self.grid_x * i + j] = []


    def populate_world(self):
        sample_list = []
        for i in range(self.grid_length):
            for j in range(self.team_size):
                sample_list.append(i)


        grid = [0 for x in range(self.grid_x * self.grid_y)]
        self.agent_states = random.sample(sample_list, self.pop)
        for i in range(len(self.agent_states)):
            self.grid_dict[self.agent_states[i]].append(i % self.no_of_teams)



    def update_step(self):
        
        old_dict = self.grid_dict
        self.initialize_grid()
        for i in range(self.pop):
            friendlies = old_dict[self.agent_states[i]].count(i % self.team_size)
            self.agents[i].grid_reward[self.agent_states[i]] = self.agents[i].reward_gate([friendlies, i % self.team_size])
            act = self.agents[i].get_action(self.agent_states[i])
            self.agent_states[i] = self.agent_states[i] + self.actions[act]
            self.grid_dict[self.agent_states[i]].append(i % self.no_of_teams)



if __name__ == "__main__":
    print("Training")
    world = world()
    world.initialize_grid()
    world.populate_world()
    episodes = 10
    episode_length = 100
    for j in range(episodes):
        for i in range(episode_length):
            print(world.grid_dict)
            print("epi - " + str(j))
            print("step - " + str(i))
            world.update_step()
