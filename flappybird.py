import pgzrun

TITLE = 'Flappy Bird'
WIDTH = 250
HEIGHT = 400

def draw():
    screen.blit('bg', (0,0))
    bird.draw()
    top_pipe.draw()
    bottom_pipe.draw()


def on_mouse_down():
    print('The mouse was clicked')
    bird.y -= 50

def update():
    bird.y += bird.speed

bird = Actor('bird', (75,130))
bird.speed = 1
top_pipe = Actor('pipe-upper',(150,0))
bottom_pipe = Actor('pipe-lower',(150,250))

pgzrun.go()