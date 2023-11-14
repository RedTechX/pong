from time import sleep
import pgzrun

WIDTH = 700
HEIGHT = 500

lp = Rect(7, 20, 10, 60)
rp = Rect(WIDTH - 18, 20, 10, 60)
ball_x = WIDTH/2
ball_y = HEIGHT/2
rad = 10
ys = 2
xs = 2

def draw():
    screen.clear()
    screen.draw.filled_rect(lp, (10, 100, 230))
    screen.draw.filled_rect(rp, (230, 50, 100))
    screen.draw.filled_circle((ball_x, ball_y),  rad, (255, 255, 255))

def update():
    global ball_y
    global ball_x
    global ys
    global xs
    global rad
    
    ball_y += ys
    ball_x += xs

    if ball_y > HEIGHT or ball_y < 0:
        ys = -ys

    if ball_x > WIDTH or ball_x < 0:
        xs = -xs
    
    if keyboard.space:
        lp.y -= -5
        rp.y -= -5
    
    if keyboard.b:
        lp.y -= 5
        rp.y -= 5
    
    if keyboard.w:
        lp.y -= 5
    
    if keyboard.s:
        lp.y -= -5
    
    if keyboard.i:
        rp.y -= 5
    
    if keyboard.k:
        rp.y -= -5
    
    if lp.top < 0:
        sleep(0.06)
        lp.top = 0    
    if lp.bottom > HEIGHT:
        sleep(0.06)
        lp.bottom = HEIGHT

    if rp.top < 0:
        sleep(0.06)
        rp.top = 0    
    if rp.bottom > HEIGHT:
        sleep(0.06)
        rp.bottom = HEIGHT
    
    ball_l = ball_x - rad
    ball_r = ball_x + rad
    ball_t = ball_y - rad
    ball_b = ball_y + rad
    overlap_x = ball_l < lp.right and ball_r > lp.left
    overlap_y = ball_t > lp.top and ball_b < lp.bottom
    if overlap_x and overlap_y:
        xs = -xs
    overlap_x = ball_l < rp.right and ball_r > rp.left
    overlap_y = ball_t > rp.top and ball_b < rp.bottom
    if overlap_x and overlap_y:
        xs = -xs

pgzrun.go()