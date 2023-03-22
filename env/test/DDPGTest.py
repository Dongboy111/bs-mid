import gym

## 创建一个游戏环境
env = gym.make("CartPole-v0")
## 训练20个epoch
for i in range(20):
    ## 每次训练前都初始化环境
    env.reset()
    ## 与环境的最大交互次数为100
    for step in range(100):
        ## 渲染环境
        env.render()
        ## 从 action 空间中获取一个 action
        action = env.action_space.sample()
        ## 根据 action 与环境进运行一次交互
        observation,reward,done,info = env.step(action)
        ## 如果返回当前游戏结束，推出当前游戏继续下一次训练
        if(done):
            break
