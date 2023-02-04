import board
import neopixel
import sys
import signal
import time
from time import sleep
import argparse
import random

num_pixels = 50
ORDER = neopixel.GRB
pixel_pin = board.D18
letter_delay = 1
word_delay = 3

letter_pixel = { "a": [0,1],
                 "b": [2,3],
                 "c": [4,5],
                 "d": [6,7],
                 "e": [8,9], 
                 "f": [10,11],
                 "g": [12,13],
                 "h": [14,15],
                 "i": [16,17],
                 "j": [34,33],
                 "k": [32,31],
                 "l": [30,29],
                 "m": [28,27],
                 "n": [26,25],
                 "o": [24,23],
                 "p": [22,21],
                 "q": [20],
                 "r": [19,18],
                 "s": [35,36],
                 "t": [37,38],
                 "u": [39,40],
                 "v": [41,42],
                 "w": [43,44],
                 "x": [45,46],
                 "y": [47,48],
                 "z": [49]}


parser = argparse.ArgumentParser(description='Display a message from the nether nether... Stranger Lights!')
parser.add_argument('-m', '--message', type=str, required=True, help='Type your message only a-zA-Z or spaces.')
parser.add_argument('-r', '--repeat', type=int, default=1, help='A number of times for the message to repeat.')
args = parser.parse_args()

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER)

 
def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        pixels.deinit()
        exit(1)
 
signal.signal(signal.SIGINT, handler)

def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        sleep(wait)

colors = [(255,0,0), (0,255,0), (0,0,255)]

def color_cycle():
    j=0
    while j<2:
        rainbow_cycle(0.001)
        j += 1

def display_letter(letter):
    print(letter, end='')
    sys.stdout.flush()
    pixels.fill((0,0,0))
    lights = letter_pixel[letter]
    letter_color = random_color()
    for light in lights:
        pixels[light] = letter_color
        pixels.show()
    sleep(letter_delay)
    pixels.fill((0,0,0))
    pixels.show()

def random_color():
    Green = random.randint(0,255)
    Red = random.randint(0,255)
    Blue = random.randint(0,255)
    return (Green, Red, Blue)

i = 0
while i < args.repeat:
    color_cycle()
    print(f'{i:05}-', end='')
    for letter in args.message.lower():
        if letter.isalpha():
            display_letter(letter)
        else:
            sleep(word_delay)
    color_cycle()
    i += 1
    print('')

pixels.deinit()