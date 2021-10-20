import mc_objects as mco


class World:

    def __init__(self, len_x, len_z) -> None:
        self.len_x = len_x
        self.len_z = len_z
        self.len_y = 64
        self.map = []

        self.__init_world()

    def __init_world(self) -> None:
        x = 0
        while x < self.len_x:
            y = 0
            plane = []
            while y < 14:
                new_block = mco.Block(mco.Blocks.Stone)
                plane.append([new_block] * self.len_z)
                y += 1
            while y < 16:
                new_block = mco.Block(mco.Blocks.Grass)
                plane.append([new_block] * self.len_z)
                y += 1
            while y < self.len_y:
                new_block = mco.Block(mco.Blocks.Air)
                plane.append([new_block] * self.len_z)
                y += 1

            self.map.append(plane)
            x += 1

        print("World created.")

    def place(self, block: mco.Block, x: int, y: int, z: int):
        self.map[x][y][z] = block
        print(block.name + " block placed.")

    def hit(self, tool: mco.Tool, x: int, y: int, z: int):

        block_to_break = self.map[x][y][z]
        block_tool_name = block_to_break.tool.name

        if tool.name == block_tool_name:
            air_block = mco.Block(mco.Blocks.Air)
            self.map[x][y][z] = air_block
            print(block_to_break.name + " destroyed.")
        else:
            print("Can't break "
                  + block_to_break.name
                  + " with "
                  + tool.name)
