###############################################
### SETUP ###
from tkinter import Variable
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("winter")

q1=codesters.Square(100,100,200,"Orange")
q2=codesters.Square(-100,100,200,"Red")
q3=codesters.Square(-100,-100,200,"Pink")
q4=codesters.Square(100,-100,200,"Purple")

s1=codesters.Sprite("cardinal",100,100)
s2=codesters.Sprite("pinetree",-100,-100)
s2.set_size(0.5)
s3=codesters.Sprite("Call-of-Duty-Logo",100,-100)
s3.set_size(0.12)
s4=codesters.Sprite("transparent-parakeet",-100,100)
s4.set_size(0.5)

message1=codesters.Text("Ethan",0,220,"green")
message1=codesters.Text("Fine ill do it myself",0,-220,"black")
