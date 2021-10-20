from world import World
from player import Player

import mc_objects as mco


class Game:

    def __init__(self) -> None:
        self.world = World(20, 20)
        self.player = Player(self.world)
        print("Game started.")

    def play(self):

        stone_block = mco.Block(mco.Blocks.Stone)
        pick = mco.Tool(mco.Tools.Pickaxe)
        shovel = mco.Tool(mco.Tools.Shovel)

        self.player.add_to_inv(stone_block, 0, 1)
        self.player.use(0, 16, 0)

        self.player.add_to_inv(pick, 1, 1)
        self.player.select_object(1)
        self.player.hit(0, 16, 0)
        self.player.hit(0, 15, 0)
        self.player.hit(0, 14, 0)
        self.player.hit(0, 13, 0)
        self.player.hit(0, 12, 0)
        self.player.hit(0, 11, 0)
