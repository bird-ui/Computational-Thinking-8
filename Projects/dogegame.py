#setup
import codesters,random
from codesters import StageClass
stage = StageClass()
stage.disable_all_walls()

player=codesters.Sprite("frige")
stage.set_background("gas station")
player.set_size(0.5)
player.set_x(-200)

object_speed=-0.5
kerosene=3
number_of_egg= 0

#objects
def falling_object():
    global object_speed,kerosene
    if kerosene > 0:
        x = 250
        y = random.randint(-200,200)
        object = codesters.Sprite("kayson", x, y)
        object.set_size(0.10)
        object.set_x_speed(object_speed)

# if(number_of_egg<3):
#     falling_object() 
#     number_of_egg+=1   
stage.event_interval(falling_object,9)

#collision
def collision(player,object) :
    global kerosene

    if object.get_image_name()=="kayson":
        stage.remove_sprite(object)
        kerosene-=0.5
        if kerosene==0:
            player.say(f"out of kerosene-you lose!",5)
        else:
            player.say(f"{kerosene}kerosene",0.5)

player.event_collision(collision)


#controls
def go_up():
    player.move_up(10)

player.event_key("up",go_up)

def go_down():
    player.move_down(10)

player.event_key("down",go_down)
