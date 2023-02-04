import board
import neopixel
from time import sleep 

num_pixels = 50
ORDER = neopixel.GRB 
pixel_pin = board.D18

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

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
i = 0

while i<3:
  pixels.fill((0, 0, 0))
  sleep(2)
  pixels.fill(colors[i%3])
  i += 1
  pixels.show()
  sleep(2)

j=0
while j<1000:
  rainbow_cycle(0.001)
  j += 1

pixels.deinit()
