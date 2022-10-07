import pyglet
import pyglet.gl
from pyglet.window import mouse, key
import random
import time
from include import Snake, Block


class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        init_pos_x = snake_vel * 20
        init_pos_y = snake_vel * 20

        self.food = Block(init_pos_x, init_pos_y, snake_vel,
                          color=[1., 0., 0., .6] * 4)
        self.snake = Snake(snake_vel, 0, snake_vel)

        # Board settings
        self.n_squares_x = self.width // snake_vel
        self.n_squares_y = self.height // snake_vel


        self.counter = 0
        self.best_score = 0
        self.label = pyglet.text.Label(
            '',
            font_name='Times New Roman',
            font_size=12,
            bold=True,
            x=80,
            y=self.height - 30,
            width=100,
            height=40,
            anchor_x='center',
            anchor_y='center',
            color=(255, 255, 255, 100),
            multiline=True
        )

        self.game_over = False

    def on_draw(self):

        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA,
                              pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)


        if self.snake.eaten is True:

            new_x = snake_vel * \
                random.randint(2, self.n_squares_x - 2)
            new_y = snake_vel * \
                random.randint(2, self.n_squares_y - 2)
            self.food.pos_x, self.food.pos_y = new_x, new_y

            self.food.set_vertex()
            self.snake.eaten = False

        food_vertices = pyglet.graphics.vertex_list(
            4,
            ('v2f', self.food.vertex),
            ('c4f', self.food.color)
        )
        food_vertices.draw(pyglet.gl.GL_POLYGON)


        for block in self.snake.blocks:

            if block.pos_x < 0:
                block.pos_x += self.width
            elif block.pos_x > self.width - snake_vel:
                block.pos_x = 0

            if block.pos_y < 0:
                block.pos_y += self.height
            elif block.pos_y > self.height - snake_vel:
                block.pos_y = 0

            block.set_vertex()

            snake_vertices = pyglet.graphics.vertex_list(
                4,
                ('v2f', block.vertex),
                ('c4f', block.color)
            )

            snake_vertices.draw(pyglet.gl.GL_POLYGON)

        text = 'Score:\t{}\nBest:\t{}'.format(self.counter, self.best_score)

        self.label.text = text
        self.label.draw()

    def update(self, dt):
        if self.snake.dead is False:

            head = self.snake.blocks[-1]
            dif_pos_x = abs(head.pos_x - self.food.pos_x) - snake_vel * .5
            dif_pos_y = abs(head.pos_y - self.food.pos_y) - snake_vel * .5
            if dif_pos_x <= 1. and dif_pos_y <= 1.:
                self.snake.eat(self.food.pos_x, self.food.pos_y)
                self.counter += 1

            self.snake.move_snake()
        else:
            if self.game_over is False:
                time.sleep(1)
                self.game_over = True
            self.snake.blocks = self.snake.blocks[1:]
            if len(self.snake.blocks) == 0:
                time.sleep(1)
                if self.counter > self.best_score:
                    self.best_score = self.counter
                self.counter = 0


                self.food = Block(snake_vel * 20, snake_vel *
                                  20, snake_vel, color=[1., 0., 0., .9] * 4)
                self.snake = Snake(snake_vel, 0, snake_vel)
                self.game_over = False

    def mouse(self, x, y):
        pass


if __name__ == '__main__':
    global snake_vel

    snake_vel = 20
    width, height = 800, 600

    world = MyWindow(width, height)
    pyglet.gl.glClearColor(.1, .1, .1, .1)
    world.on_draw()

    @world.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:
            world.mouse(x, y)

    @world.event
    def on_key_press(symbol, modifiers):

        if symbol == key.UP or symbol == key.W:
            world.snake.change_vel(0, snake_vel)
        if symbol == key.DOWN or symbol == key.S:
            world.snake.change_vel(0, -snake_vel)
        if symbol == key.RIGHT or symbol == key.D:
            world.snake.change_vel(snake_vel, 0)
        if symbol == key.LEFT or symbol == key.A:
            world.snake.change_vel(-snake_vel, 0)

    pyglet.clock.schedule_interval(world.update, 1 / 20.)
    pyglet.app.run()
