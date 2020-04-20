import numpy as np
import random
import brain


class World:
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
        self.agents = [brain.Brain(self.grid_length,self.team_size,self.actions) for x in range(self.pop)]

    def initialize_grid(self):
        for i in range(self.grid_y):
            for j in range(self.grid_x):
                self.grid_dict[self.grid_x * i + j] = [0 for x in range(self.team_size)]

    def populate_world(self):
        sample_list = []
        for i in range(self.grid_length):
            for j in range(self.team_size):
                sample_list.append(i)

        grid = [0 for x in range(self.grid_x * self.grid_y)]
        self.agent_states = random.sample(sample_list, self.pop)

    def update_step(self):
        for i in range(self.pop):
            act = brain.get_action(type='policy')
            self.action(i, act)

    def action(self, agent, act):
        action_check = self.actions[act]
        fut_state = self.agent_states[agent] + self.actions[act]
        if action_check == 1 or -1:
            if action_check == 1 and fut_state % self.grid_x == 0:
                new_sample_act = brain.get_action(type='random')
                return self.action(agent, new_sample_act)
            elif action_check == -1 and fut_state % self.grid_y == self.grid_x - 1:
                new_sample_act = brain.get_action(type='random')
                return self.action(agent, new_sample_act)
        elif fut_state > 0 or fut_state < self.grid_length:
            new_sample_act = brain.get_action(type='random')
            return self.action(agent, new_sample_act)
