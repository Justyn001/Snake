import pygame as pg
import sys
import random

class Snake:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((400, 300))
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('Nimbus Roman No9 L', 30)
        self.position = None
        self.snake_x, self.snake_y = 200, 150
        self.direction = None
        self.snake_length = None
        self.food = True
        self.food_x, self.food_y = 300, 80
        self.game_status = False
        self.best_score = 0
        self.epoch_counter = 0
        self.fps = 30
        self.moves = 0
        self.restart()


    def restart(self):
        self.moves = 0
        self.direction = random.choice([0, 1, 2, 3])
        self.position = [(200, 150), (200, 160), (200, 170)]
        self.snake_x: int = 200
        self.snake_y: int = 150
        self.snake_length: int = 3
        self.food_logic()
        self.game_status = True

    def event_handler(self, move_direction):
        self.game_status = True
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.fps = 15 if self.fps == 30 else 30

        if self.direction == 0 and move_direction != 1:
            self.direction = move_direction
        elif self.direction == 1 and move_direction != 0:
            self.direction = move_direction
        elif self.direction == 2 and move_direction != 3:
            self.direction = move_direction
        elif self.direction == 3 and self.direction != 2:
            self.direction = move_direction

            # elif event.type == pg.KEYDOWN and event.key == pg.K_UP and self.direction != 1:
            #     self.direction = 0
            # elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN and self.direction != 0:
            #     self.direction = 1
            # elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT and self.direction != 3:
            #     self.direction = 2
            # elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT and self.direction != 2:
            #     self.direction = 3

    def update(self):
        self.clock.tick(self.fps)
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
        if (self.snake_x < 0 or self.snake_x > 390
                or self.snake_y < 0 or self.snake_y > 290):
            self.game_status = False

        for i in range(1, self.snake_length):
            if self.snake_x == self.position[i][0] and self.snake_y == self.position[i][1]:
                self.game_status = False
                break

        # if self.moves > 500:
        #     self.game_status = False

    def snake_logic(self):
        if (self.food_x == self.snake_x) and (self.food_y == self.snake_y):
            self.snake_length += 1
            self.food = False
            self.moves = 0
        else:
            self.moves += 1

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
            self.food_x: int = random.randrange(1, 39) * 10
            self.food_y: int = random.randrange(1, 29) * 10
            self.food = True

    def food_draw(self):
        if self.food:
            pg.draw.rect(self.screen, "green", (self.food_x, self.food_y, 10, 10), 0)

    def points_draw(self):
        score = self.font.render(f"Score: {self.snake_length - 3}", True, "white")

        self.best_score = self.snake_length - 3 if self.snake_length - 3 > self.best_score else self.best_score
        best_score_display = self.font.render(f"Best Score: {self.best_score}", True, "white")

        epoch = self.font.render(f"Epoch: {self.epoch_counter}", True, "white")

        self.screen.blit(score, (0, 0))
        self.screen.blit(best_score_display, (0, 20))
        self.screen.blit(epoch, (0, 40))

    def run(self, action):
        if not self.game_status:
            print(f"Game: {self.epoch_counter} Score: {self.snake_length - 3} Best score: {self.best_score}")
            self.restart()
            self.epoch_counter += 1
        self.event_handler(action)
        self.update()
        self.draw()


