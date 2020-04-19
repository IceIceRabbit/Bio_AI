import MGA
class Brain:
    def __init__(self,grid_length,team_size,actions):
        # self.gates = []
        self.grid_reward = [0 for x in range(grid_length)]
        self.team_size = team_size
        self.actions = actions

    def surrounding_rewards(self, state):
        x = state[0] #state[0] = x, state[1] = y
        y = state[1]
        here = y + self.grid_length*x
        up = y + self.grid_length*(x+1)
        down = y + self.grid_length*(x-1)
        right = (y+1) + self.grid_length*x
        left = (y-1) + self.grid_length*x
        fitness = [self.grid_reward(here), self.grid_reward(up), self.grid_reward(down), self.grid_reward(right), self.grid_reward(left)]
        return fitness
        
    def get_action(self,state,fitness):

        action = MGA.get_action(fitness)



    def reward_gate(self,inputs):
        net_reward = 0
        grid_location = inputs[0][1]
        friendlies = int(inputs[0])
        net_reward = pow(10,friendlies)



        0 1 0
        0 - 0
        0 0 0
