from typing import Tuple, Optional, Union, List

import gym
from gym.core import RenderFrame


class BaseEnv(gym.Env):
    def __init__(self):
        super.__init__()
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