import torch
from torch import nn
import nn.functional as F
import numpy as np
from game_env import Main

# RL model


class QEnv(Main):
    def __init__(self):
        super().__init__()


# Вход - 8 лучей до стен + 8 до других машин + место(1, 2, 3 и т д)
# Выход - 2 нейрона: увеличить уменьшить скороть и увеличить уменьшить угол поворота руля


class QNetwork(nn.Module):
    def __init__(self, lr):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(in_features=17, out_features=64),
            nn.ReLU(),
            nn.Linear(in_features=64, out_features=2),
        )


class QAgent():
    def __init__(self, env, discount_rate = 0.97, lr = 0.0001):
        self.eps = 1
        self.discount_rate = discount_rate
        self.learning_rate = learning_rate
        self.network = QNetwork(self.learning_rate)

    def get_action(self):
