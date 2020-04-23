import sys
sys.path.insert(0, r'C:\Users\manas\Documents\Codes\BioAI\Final')
import world
from MGA import MGA

class brain:
    
    def __init__(self,grid_length,team_size,actions, agent_states, grid_x, grid_y):
        # self.gates = []
        self.grid_reward = [0 for x in range(grid_length)]
        self.team_size = team_size
        self.actions = actions
        self.friends = 0
        self.mga = MGA(grid_length, self.grid_reward, self.actions, agent_states, grid_x, grid_y)


    def get_action(self,state):
        
        action = self.mga.move(0.9, state)
        return action


    def reward_gate(self,inputs):
        net_reward = 0
        friendlies = inputs[0]
        team = inputs[1]
        if friendlies:
            net_reward = pow(team + 1,friendlies)
        return net_reward
