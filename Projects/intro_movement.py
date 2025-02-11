# setup
import codesters 
from codesters import StageClass
stage = StageClass ()

stage.set_background("moon")
s1 = codesters.Sprite("person1" ,0,-200)
s1.set_size(0.5)

# control set
def move_up (sprite):
    sprite.move_up(10)

def move_down(sprite):
    sprite.move_down(10)

def move_right(sprite):
    sprite.move_right(10)

def move_left(sprite):
    sprite.move_left(10)

def show(sprite):
    sprite.show()

def turn_left(sprite):
    heading = sprite.heading
    sprite.set_heading(heading + 100)

def turn_right(sprite):
    heading = sprite.heading
    sprite.set_heading(heading - 100)

def forward(sprite):
    sprite.forward(1)

# define hide and show
def hide (sprite):
    sprite.hide()

#bind controls 
s1.event_key("w",move_up)
s1.event_key("s",move_down)
s1.event_key("a",move_left)
s1.event_key("d",move_right)
s1.event_key("h",hide)
s1.event_key("g",show)
s1.event_key("w",turn_left)
s1.event_key("a",turn_right)
s1.event_key("s",forward)

for i in range(100000):
    s1.set_heading(i+10)
#reminder message
print("game has started. open the screen using ports to play")
