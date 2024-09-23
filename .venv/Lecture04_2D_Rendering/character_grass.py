from pico2d import *
from math import *
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
dx=0
dy=0
cir_dx=0
cir_dy=0
while True:
    while dx<100:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(dx + 400, 90)
        dx+=2
        delay(0.01)
    while (dx>0 and dy<173):
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(dx + 400, dy + 90)
        dx-=1
        dy+=tan(60/180*pi)
        delay(0.01)
    while (dx>-100 and dy>0):
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(dx + 400, dy + 90)
        dx-=1
        dy-=tan(60/180*pi)
        delay(0.01)
    while dx<0:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(dx + 400, 90)
        dx+=2
        delay(0.01)

    for angle in range(270, 630):
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(cir_dx + 400, cir_dy + 190)
        cir_dx = cos(angle/180*pi)*100
        cir_dy = sin(angle/180*pi)*100
        delay(0.01)
a= input()
