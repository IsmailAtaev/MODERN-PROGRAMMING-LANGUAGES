class Block:
    def __init__(self, pos_x, pos_y, size, color=[0, 1., 0, 1.] * 4):
        self.pos_x = pos_x + size
        self.pos_y = pos_y + size

        self.size = size
        self.vertex = []
        self.color = color

        self.red_size = 3  # Reduce the size on draw a little bit

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def set_vertex(self):
        self.vertex = []
        # Add the four vertex to the vertex list
        self.vertex.append(self.pos_x + self.red_size)
        self.vertex.append(self.pos_y + self.red_size)

        self.vertex.append(self.pos_x + self.red_size)
        self.vertex.append(self.pos_y + self.size - self.red_size)

        self.vertex.append(self.pos_x + self.size - self.red_size)
        self.vertex.append(self.pos_y + self.size - self.red_size)

        self.vertex.append(self.pos_x + self.size - self.red_size)
        self.vertex.append(self.pos_y + self.red_size)


class Snake:
    def __init__(self, vel_x, vel_y, size):
        # The snake starts with just two blocks
        init_pos = 5 * vel_x
        self.head_color = [.5, 8., .6, 1.] * 4
        self.tail_color = [.0, 1., .0, 1.] * 4
        self.blocks = [
            Block(pos_x=-2 * vel_x + init_pos, pos_y=init_pos, size=size,
                  color=self.tail_color),
            Block(pos_x=-vel_x + init_pos, pos_y=init_pos, size=size,
                  color=self.tail_color),
            Block(pos_x=init_pos, pos_y=init_pos,
                  size=size, color=self.head_color)
        ]

        self.vel_x, self.vel_y = vel_x, vel_y
        self.dead = False
        self.size = size

        self.eaten = True

    def move_snake(self):

        self.check_block_pos()

        # Move the tail
        for i in range(len(self.blocks) - 1):
            next_block = self.blocks[i + 1]
            dif_x = next_block.pos_x - self.blocks[i].pos_x
            dif_y = next_block.pos_y - self.blocks[i].pos_y

            self.blocks[i].move(dif_x, dif_y)

        # Move the head
        self.blocks[-1].move(self.vel_x, self.vel_y)

        return True

    def change_vel(self, vel_x, vel_y):
        next_head_pos_x = self.blocks[-1].pos_x + vel_x
        next_head_pos_y = self.blocks[-1].pos_y + vel_y

        # Check if we are trying to move backwards
        dif_x = abs(next_head_pos_x - self.blocks[-2].pos_x)
        dif_y = abs(next_head_pos_y - self.blocks[-2].pos_y)
        if dif_x > 1. and dif_y > 1.:
            self.vel_x = vel_x
            self.vel_y = vel_y

    def check_block_pos(self):

        next_head_pos_x = self.blocks[-1].pos_x + self.vel_x
        next_head_pos_y = self.blocks[-1].pos_y + self.vel_y

        for block in self.blocks[:-2:]:
            dif_x = abs(next_head_pos_x - block.pos_x)
            dif_y = abs(next_head_pos_y - block.pos_y)
            if dif_x <= 1. and dif_y <= 1.:
                self.dead = True
                return False

        return True

    def eat(self, x_food, y_food):
        self.blocks.append(
            Block(x_food - self.size, y_food - self.size, self.size))
        self.blocks[-2].color = self.tail_color
        self.blocks[-1].color = self.head_color
        self.eaten = True


def main():
    # snk = Snake()
    pass


if __name__ == '__main__':
    main()
