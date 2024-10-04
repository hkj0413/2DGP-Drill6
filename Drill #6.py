from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
ranx, rany = random.randint(21, 1256), random.randint(52, 998)
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
MoveRight = True
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if MoveRight == True:
        character.clip_draw(frame * 100, 100, 100, 100, x, y, 100, 100)
    elif MoveRight == False:
        character.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', x, y, 100, 100)

    hand_arrow.clip_draw(0, 0, 50, 52, ranx, rany)
    update_canvas()
    frame = (frame + 1) % 8

    if x < ranx and y < rany:
        x += (ranx - x) / 100
        y += (rany - y) / 100
        MoveRight = True
    elif x > ranx and y < rany:
        x -= (x - ranx) / 100
        y += (rany - y) / 100
        MoveRight = False
    elif x < ranx and y > rany:
        x += (ranx - x) / 100
        y -= (y - rany) / 100
        MoveRight = True
    elif x > ranx and y > rany:
        x -= (x - ranx) / 100
        y -= (y - rany) / 100
        MoveRight = False
    if ranx - x < 1 and ranx - x > -1 and rany - y < 1 and rany - y > -1:
        ranx, rany = random.randint(21, 1256), random.randint(52, 998)

    handle_events()

close_canvas()