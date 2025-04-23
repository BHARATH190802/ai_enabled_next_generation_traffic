# Import GYM stuff
import gym
from gym.spaces import Box

# Import helpers
import numpy as np
import random
import os

# Import Stable baselines stuff
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common. evaluation import evaluate_policy


class traffic_env(gym.Env):

    def __init__(self):
        self.action_space = Box(low=10, high=90, shape=(1,))
        self.observation_space= Box(low=0, high=100, shape=(3,))
        self.capacity = Box(low=20, high=800, shape=(1,)).sample()
        # self.prev , self.next = Box(low=0, high=100, shape=(2,)).sample()
        self.hops=0

        # self.state=den_calc(model(path+files[self.hops]),self.capacity)
        self.state=Box(low=20, high=800, shape=(3,)).sample()

        self.flow_rate=10



    def step(self, action):

        p,c,n=self.state
        # print("Before C:",c,self.hops+1)
        # p,n = self.prev , self.next
        nv=action*self.flow_rate/100

        c-=nv*(1-p*0.23)+random.uniform(-10.0, +13.0)
        n+= nv*0.45 - random.uniform(-10.0, +13.0)
        p+=random.uniform(-10.0, +13.0)


  # Reward System

        metric=int(c/25)
        if(metric==0):
            reward=1
        elif(metric==3):
            reward=-1
        else:
            reward=0

        self.hops+=1
        done= True if self.hops==60 else False

        return self.state,reward,done,{}

        # if done :
        #   return 0,reward,done,{}
        # else:
        #   return den_calc(model(path+files[self.hops]),self.capacity), reward, done, {}


    def render (self):
        pass

    def reset(self):
        self.state = Box(low=0, high=100, shape=(3,)).sample()
        self.hops=60
        return self.state