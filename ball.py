from pico2d import *
import game_world
import game_framework
import random
import server

class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        randrange_x = 0, server.background.w
        randrange_y = 0, server.background.h
        self.x = x if x else random.randint(*randrange_x)
        self.y = y if y else random.randint(*randrange_y)

        self.draw_x = self.x - server.background.window_left
        self.draw_y = self.y - server.background.window_bottom

    def draw(self):
        self.draw_x = self.x - server.background.window_left
        self.draw_y = self.y - server.background.window_bottom
        self.image.draw(self.draw_x, self.draw_y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                other.ball = self # 소년이 볼을 소유하도록.
                pass
            case 'zombie:ball':
                other.ball = self