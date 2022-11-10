from typing import Tuple, Optional, Union, List
from gym import spaces
import gym
from gym.core import RenderFrame




R = 8.1314



class BaseEnv():
    def __init__(self):
        super(BaseEnv,self).__init__()
        self.action_space = spaces.Discrete(100)      #动作数量
        self.observation_space = spaces.Discrete(1000)#观察空间
        self.tempActionValue = [] #经过调整的未知参数数值
        self.baseAdjuseValue = [] #每个参数调整基准
        self.baseRangeValue = [[] for _ in range(self.action_space.n)] #每个参数的调整最小最大范围  [[]]*n
    def step(self, action: list) -> Tuple[list, float, bool, bool, dict]:
        """

        :param action:需要调整的参数是对未确定参数向大调还是小调 1 代表向大调整，0代表向小调整
        :return: 四元组
        """




        # pass
    def reset(self):
        pass
if __name__ == "__main__":
    dong = BaseEnv()
    dong.step([_ for _ in range(dong.action_space.n)])