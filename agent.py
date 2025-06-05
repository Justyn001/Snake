import torch
import random
import numpy as np
from collections import deque
from model import AiModel

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:
    def __init__(self):
        self.model = AiModel()
        self.target_model = AiModel()
        self.target_model.load_state_dict(self.model.state_dict())
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=LR)
        self.memory = deque(maxlen=MAX_MEMORY)
        self.gamma = 0.9
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.n_games = 0

    def get_state(self, game):
        head_x, head_y = game.snake_x, game.snake_y

        point_l = (head_x - 10, head_y)
        point_r = (head_x + 10, head_y)
        point_u = (head_x, head_y - 10)
        point_d = (head_x, head_y + 10)

        dir_l = game.direction == 2
        dir_r = game.direction == 3
        dir_u = game.direction == 0
        dir_d = game.direction == 1

        danger_straight = (
            (dir_r and point_r in game.position) or
            (dir_l and point_l in game.position) or
            (dir_u and point_u in game.position) or
            (dir_d and point_d in game.position)
        )

        danger_right = (
            (dir_u and point_r in game.position) or
            (dir_d and point_l in game.position) or
            (dir_l and point_u in game.position) or
            (dir_r and point_d in game.position)
        )

        danger_left = (
            (dir_d and point_r in game.position) or
            (dir_u and point_l in game.position) or
            (dir_r and point_u in game.position) or
            (dir_l and point_d in game.position)
        )

        food_left = game.food_x < head_x
        food_right = game.food_x > head_x
        food_up = game.food_y < head_y
        food_down = game.food_y > head_y

        state = [
            danger_straight,
            danger_right,
            danger_left,

            dir_l,
            dir_r,
            dir_u,
            dir_d,

            food_left,
            food_right,
            food_up,
            food_down
        ]

        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_short_memory(self, state, action, reward, next_state, done):
        self._train_step(state, action, reward, next_state, done)

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory

        for state, action, reward, next_state, done in mini_sample:
            self._train_step(state, action, reward, next_state, done)

    def _train_step(self, state, action, reward, next_state, done):
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)

        pred = self.model(state)
        target = pred.clone().detach()

        with torch.no_grad():
            next_pred = self.target_model(next_state)
            target[action] = reward + (0 if done else self.gamma * torch.max(next_pred))

        self.optimizer.zero_grad()
        loss = torch.nn.functional.mse_loss(pred, target)
        loss.backward()
        self.optimizer.step()

    def act(self, state):
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        if random.random() < self.epsilon:
            return random.randint(0, 3)
        state_tensor = torch.tensor(state, dtype=torch.float)
        with torch.no_grad():
            return torch.argmax(self.model(state_tensor)).item()
