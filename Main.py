import pygame as pg
import sys
import random

class Snake:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((1400, 800))
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('Nimbus Roman No9 L', 30)
        self.position = [(690, 390), (690, 400), (690, 410)]
        self.snake_x: int = 690
        self.snake_y: int = 390
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

            elif event.type == pg.KEYDOWN and event.key == pg.K_UP and self.direction != 1:
                self.direction = 0
            elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN and self.direction != 0:
                self.direction = 1
            elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT and self.direction != 3:
                self.direction = 2
            elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT and self.direction != 2:
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
        self.points_draw()
        pg.display.update()

    def check_collision(self):
        if (self.snake_x < 0 or self.snake_x > 1410
                or self.snake_y < 0 or self.snake_y > 810):
            self.position = [(690, 390), (690, 405), (690, 415)]
            self.snake_length = 3
            self.snake_x = 690
            self.snake_y = 390
            self.direction = 0

        for i in range(1, self.snake_length):
            if self.snake_x == self.position[i][0] and self.snake_y == self.position[i][1]:
                self.position = [(690, 390), (690, 400), (690, 410)]
                self.snake_length = 3
                self.snake_x = 690
                self.snake_y = 390
                self.direction = 0
                break

    def snake_logic(self):
        if (self.food_x == self.snake_x) and (self.food_y == self.snake_y):
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

        coordinates = (self.snake_x, self.snake_y)

        if self.food:
            self.position.insert(0, coordinates)
            self.position.pop(-1)
        else:
            self.position.insert(0, coordinates)

    def snake_draw(self):
        for x in self.position:
            pg.draw.rect(self.screen, "grey", (x[0], x[1], 10, 10), 0)

    def food_logic(self):
        if not self.food:
            self.food_x: int = random.randrange(1, 135) * 10
            self.food_y: int = random.randrange(1, 75) * 10
            self.food = True

    def food_draw(self):
        if self.food:
            pg.draw.rect(self.screen, "green", (self.food_x, self.food_y, 10, 10), 0)

    def points_draw(self):
        score = self.font.render(f"Score: {self.snake_length - 3}", True, "white")
        self.screen.blit(score, (0, 0))

    def run(self):
        while True:
            self.event_handler()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Snake()
    game.run()

