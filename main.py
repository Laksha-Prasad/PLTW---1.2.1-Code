# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
#painter.fillcolor("dark green")
air_color = ("dark green")
#painter.size(5)
air_size = 5
air_shape = ("arrow")

#-----initialize turtle-----
air = trtl.Turtle()

#-----game functions--------
air.color(air_color)
air.shapesize(air_size)
air.shape(air_shape)

def air_clicked(x, y):
	print("Air was clicked!")

score = 0
def change_score():
  global score
  score += 1
  print("Score: " ,score)

def change_position(x,y):
  xpos = rand.randint(-200, 200)
  ypos = rand.randint(-150,150)
  air.penup()
  air.goto(xpos,ypos)
  print("Air was clicked!")
  change_score()

#-----events----------------
air.onclick(change_position)

wn = trtl.Screen()
wn.mainloop()