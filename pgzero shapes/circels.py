import pgzrun
import random
WIDTH=300
HEIGHT=300
def draw():
    x=150
    y=150
    radius=5
    startingcenter=x,y
    screen.fill('dark red')
    for i in range (5):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        screen.draw.circle(startingcenter,radius,(r,g,b))
        radius=radius+5
        
pgzrun.go()

    

