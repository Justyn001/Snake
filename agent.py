import random

import torch

from game import Snake
from model import AiModel

class Agent:
    def __init__(self, game):
        self.actions = [0, 1, 2, 3]
        self.game = game
        self.memory = [self.get_position()]

    def get_position(self):
        snake_x, snake_y = self.game.snake_x, self.game.snake_y
        direction = self.game.direction
        food_x, food_y = self.game.food_x, self.game.food_y
        position = self.game.position
        danger_list = self.check_danger(position, snake_x, snake_y)
        reward: int = 0
        if not self.game.food and self.game.food_y is None:
            reward += 10
        if not game.game_status:
            reward -= 10

        return [snake_x, snake_y, direction, food_x, food_y, *danger_list, reward]

    def check_danger(self, snake_position, snake_x, snake_y) -> list:
        danger_list = []

        danger_list.append(1) if snake_y-10 < 0 or snake_y - 10 in [x[1] for x in snake_position]\
            else danger_list.append(0)
        danger_list.append(1) if snake_y+10 > 790 or snake_y + 10 in [x[1] for x in snake_position]\
            else danger_list.append(0)
        danger_list.append(1) if snake_x-10 < 0 or snake_x - 10 in [x[0] for x in snake_position]\
            else danger_list.append(0)
        danger_list.append(1) if snake_x+10 > 1390 or snake_x + 10 in [x[0] for x in snake_position]\
            else danger_list.append(0)

        return danger_list

    def choose_action(self) -> int:
        random_move = random.randrange(0, 4)
        return random_move

    def store_experience(self):
        self.memory.insert(0, self.get_position())
        if len(self.memory) > 2:
            self.memory.pop(-1)


    def run(self):
        self.get_position()
        self.choose_action()
        self.store_experience()
        print(self.memory)

def train():
    X = agent.memory
    data = torch.tensor(X)
    y_pred = model(data)
    print(y_pred)

if __name__ == "__main__":
    game = Snake()
    agent = Agent(game)
    model = AiModel()
    while True:
        game.run(agent)
        agent.run()
        train()
        print(game.game_status)
        
        




















