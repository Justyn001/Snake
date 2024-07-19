import pygame as pg
import sys
import random


class Snake:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((1400, 800))
        self.clock = pg.time.Clock()
        self.position = [(695, 395), (695, 405), (695, 415)]
        self.snake_x: int = 695
        self.snake_y: int = 395
        self.direction: int = 0
        self.snake_length: int = 3
        self.food: bool = False
        self.food_x: int = 0
        self.food_y: int = 0

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN and event.key == pg.K_UP and self.direction != 1:
                self.direction = 0
            if event.type == pg.KEYDOWN and event.key == pg.K_DOWN and self.direction != 0:
                self.direction = 1
            if event.type == pg.KEYDOWN and event.key == pg.K_LEFT and self.direction != 3:
                self.direction = 2
            if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT and self.direction != 2:
                self.direction = 3

    def update(self):
        self.clock.tick(30)
        fps: float = round(self.clock.get_fps(), 1)
        pg.display.set_caption(f"Sssnake   {fps}")
        self.snake_logic()
        self.food_logic()
        self.check_collision()

    def draw(self):
        self.screen.fill("black")
        self.snake_draw()
        self.food_draw()
        pg.display.update()

    def check_collision(self):
        if (self.snake_x <= 0 or self.snake_x >= 1410
                or self.snake_y <= 0 or self.snake_y >= 810):
            self.position = [(695, 395), (695, 405), (695, 415)]
            self.snake_length = 3
            self.snake_x = 695
            self.snake_y = 395
            self.direction = 0

        for i in range(1, len(self.position)):
            if self.snake_x == self.position[i][0] and self.snake_y == self.position[i][1]:
                self.position = [(695, 395), (695, 405), (695, 415)]
                self.snake_length = 3
                self.snake_x = 695
                self.snake_y = 395
                self.direction = 0

    def snake_logic(self):
        for i in range(10):
            if ((self.food_x <= self.snake_x + i <= self.food_x + 10) and
                    (self.food_y <= self.snake_y + i <= self.food_y + 10)):
                self.snake_length += 1
                self.food = False

        if self.direction == 0:
            self.snake_y -= 10
        elif self.direction == 1:
            self.snake_y += 10
        elif self.direction == 2:
            self.snake_x -= 10
        elif self.direction == 3:
            self.snake_x += 10

        cordinates = (self.snake_x, self.snake_y)

        if self.food:
            self.position.insert(0, cordinates)
            self.position.pop(-1)
        else:
            self.position.insert(0, cordinates)

    def snake_draw(self):
        for x in self.position:
            pg.draw.rect(self.screen, "red", (x[0], x[1], 10, 10), 0)

    def food_logic(self):
        if not self.food:
            self.food_x: int = random.randrange(1, 135) * 10
            self.food_y: int = random.randrange(1, 75) * 10
            self.food = True

    def food_draw(self):
        if self.food:
            pg.draw.rect(self.screen, "green", (self.food_x, self.food_y, 10, 10), 0)

    def run(self):
        while True:
            self.event_handler()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Snake()
    game.run()

