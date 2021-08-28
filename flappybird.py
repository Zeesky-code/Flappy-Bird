import pgzrun

TITLE = 'Flappy Bird'
WIDTH = 250
HEIGHT = 400

def update():
    bird.speed += gravity
    bird.y += bird.speed
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed
    if top_pipe.right < 0:
        top_pipe.left = WIDTH
        bottom_pipe.left = WIDTH
    if bird.y > HEIGHT:
        reset()
    if (bird.colliderect(top_pipe )) or (bird.colliderect(bottom_pipe )):
        hit_pipe()
    if top_pipe.right < bird.x:
        bird.score += 1


def draw():
    screen.blit('bg', (0,0))
    bird.draw()
    top_pipe.draw()
    bottom_pipe.draw()
    screen.draw.text(
    str(0),
    color='white',
    midtop =(20, 10),
    fontsize=70,
    )


def on_mouse_down():
    if (bird.alive):
        bird.speed = -6.5


def reset():
    print('Back to the start...')
    bird.speed = 1
    bird.center = (75, 100)
    bird.image = 'bird'
    bird.alive = True
    top_pipe.center = (150, 0)
    bottom_pipe.center = (150, top_pipe.height + gap)
    top_pipe.pair_number = 1
    

def hit_pipe():
    print('Hit pipe!')
    bird.image = 'ghost_bird'
    bird.alive = False



bird = Actor('bird', (75,130))
gap = 140
top_pipe = Actor('pipe-upper',(150,0))
bottom_pipe = Actor('pipe-lower',(150,top_pipe.height + gap))
scroll_speed = -1
gravity = 0.3
bird.score = 0


reset()
pgzrun.go()