import .world
import .MGA
class Brain:
    def __init__(self,grid_length,team_size,actions):
        # self.gates = []
        self.grid_reward = [0 for x in range(grid_length)]
        self.team_size = team_size
        self.actions = actions
        self.friends = 0
        
    def get_action(self,state):
        action = MGA.get_action(state)
        return action




    def reward_gate(self,inputs):
        net_reward = 0
        friendlies = inputs[0]
        team = inputs[1]
        if friendlies:
            net_reward = pow(team + 1,friendlies)
        return net_reward




