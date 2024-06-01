import pgzrun
import random
WIDTH=300
HEIGHT=300
def draw():
    screen.fill('darkblue')
    w=250
    h=50
    

    for i in range (20):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        rect=Rect((0,0),(w,h))
        rect.center=150,150
        screen.draw.rect(rect,(r,g,b))
        w=w-10
        h=h+10


pgzrun.go()
