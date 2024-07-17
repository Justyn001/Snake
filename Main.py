import pygame as pg
import sys
import random

class Snake:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((1400, 800))
        self.clock = pg.time.Clock()
        self.running = False
        self.position = [(695, 395)]
        self.snake_x: int = 695
        self.snake_y: int = 395
        self.direction: int = 0
        self.snake_length: int = 1
        self.food: bool = False
        self.food_x: int = 0
        self.food_y: int = 0
    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                self.direction = 0
            if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                self.direction = 1
            if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                self.direction = 2
            if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                self.direction = 3

    def update(self):
        self.clock.tick(120)
        fps: float = round(self.clock.get_fps(), 1)
        pg.display.set_caption(f"Sssnake   {fps}")
        self.snake_logic()
        self.food_logic()

    def draw(self):
        self.screen.fill("black")
        self.snake_draw()
        self.food_draw()
        pg.display.update()

    def snake_logic(self):
        for i in range(10):
            if ((self.food_x <= self.snake_x + i <= self.food_x + 10) and
                    (self.food_y <= self.snake_y + i <= self.food_y + 10)):
                self.snake_length += 1
                self.food = False

        if self.direction == 0:
            self.snake_y -= 2
        elif self.direction == 1:
            self.snake_y += 2
        elif self.direction == 2:
            self.snake_x -= 2
        elif self.direction == 3:
            self.snake_x += 2

    def snake_draw(self):
        y_pos = 0
        snake_legnth: int = 1
        for x in range(snake_legnth):
            pg.draw.rect(self.screen, "red", (self.snake_x, self.snake_y + y_pos, 10, 10), 2)
            #print(f"{self.x, self.y}")
            #y_pos += 10

    def food_logic(self):
        if not self.food:
            self.food_x: int = random.randrange(0, 1350)
            self.food_y: int = random.randrange(0, 750)
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


