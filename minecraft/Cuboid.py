__author__ = 'jeffgarrison'

import minecraft
import block
import random


class Cuboid:
    def __init__(self, width=10, height=10, length=10, block_type=block.GLASS, startx=0, starty=0, startz=0,
                 random=False, state=0):
        """


        """
        self.width = width
        self.height = height
        self.length = length
        self.solid = False
        self.block = block_type
        self.mc = minecraft.Minecraft.create()
        self.startx = startx
        self.starty = starty
        self.startz = startz
        self.random = random
        self.state = state

    def draw(self):

        for x in range(self.width):
            for y in range(self.height):
                for z in range(self.length):
                    if x == 0 or x == self.width-1 or y == 0 or y == self.height-1 or z == 0 or z == self.length-1:
                        if self.random is True:
                            self.block = block.Block(random.randint(1, 98))

                        self.mc.setBlock(x+self.startx, y+self.starty, z+self.startz, self.block, self.state)
                        self.mc.postToChat("state=" + str(self.state))