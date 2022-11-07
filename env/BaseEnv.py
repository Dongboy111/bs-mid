from typing import Tuple, Optional, Union, List
from gym import spaces
import gym
from gym.core import RenderFrame







class BaseEnv(gym.Env):
    def __init__(self):
        super(BaseEnv,self).__init__()
        self.action_space = spaces.Discrete(100)      #动作数量
        self.observation_space = spaces.Discrete(1000)#观察空间
    def step(self, action: list) -> Tuple[list, float, bool, bool, dict]:

        pass
    def __getstate__(self):
        pass
    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[dict] = None,
    ) -> Tuple[list, dict]:
        pass
    def render(self) -> Optional[Union[RenderFrame, List[RenderFrame]]]:
        pass