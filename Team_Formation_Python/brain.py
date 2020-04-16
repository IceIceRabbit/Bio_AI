import MGA
class Brain:
    def __init__(self,grid_length,team_size,actions):
        # self.gates = []
        self.grid_reward = [0 for x in range(grid_length)]
        self.team_size = team_size
        self.actions = actions

    def get_action(self,state,fitness):
        fitness =
        action = MGA.get_action(fitness)




    def reward_gate(self,inputs):
        net_reward = 0
        grid_location = inputs[0][1]
        friendlies = int(inputs[0])
        net_reward = pow(10,friendlies)



        0 1 0
        0 - 0
        0 0 0