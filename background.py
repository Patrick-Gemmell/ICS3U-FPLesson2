#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: Sep 2019
# This program draws a background on the PyBadge

import ugame
import stage

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("ball.bmp")


def main():
    # this function sets the background

    # sets the background to image 0 in the bank
    # DO NOT have the 0th image as clear, BAD things will happen!
    background = stage.Grid(image_bank_1, 10, 8)
    # changes (0,0) image to the 3rd image
    background.tile(0, 0, 3)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    while True:
        # repeat forever, or you turn it off!
        pass


if __name__ == "__main__":
    main()
