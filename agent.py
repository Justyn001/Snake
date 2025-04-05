import random

class Agent:
    def __init__(self):
        self.actions = [0, 1, 2, 3]
        self.memory = []

    def get_position(self, game):
        snake_x, snake_y = game.snake_x, game.snake_y
        direction = game.direction
        food_x, food_y = game.food_x, game.food_y
        position = game.position
        danger_list = self.check_danger(position, snake_x, snake_y)

        return [snake_x, snake_y, direction, food_x, food_y, *danger_list]

    def check_danger(self, position, snake_x, snake_y) -> list:
        danger_list = []

        danger_list.append(1) if snake_y-10 < 0 or snake_y - 10 in [x[1] for x in position]\
            else danger_list.append(0)
        danger_list.append(1) if snake_y+10 > 790 or snake_y + 10 in [x[1] for x in position]\
            else danger_list.append(0)
        danger_list.append(1) if snake_x-10 < 0 or snake_x - 10 in [x[0] for x in position]\
            else danger_list.append(0)
        danger_list.append(1) if snake_x+10 > 1390 or snake_x + 10 in [x[0] for x in position]\
            else danger_list.append(0)

        return danger_list

    def choose_action(self) -> int:
        random_move = random.randrange(0, 4)
        return random_move

    def store_experience(self):
        self.memory.append(self.get_position())
























