

class Agent:
    def __init__(self):
        self.actions = [0, 1, 2, 3]
        self.memory = []

    def get_position(self, game):
        snake_x, snake_y = game.snake_x, game.snake_y
        direction = game.direction
        food_x, food_y = game.food_x, game.food_y
        danger_list = game.check_danger(direction, snake_x, snake_y)
