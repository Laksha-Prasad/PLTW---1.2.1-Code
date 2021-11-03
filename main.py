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

def change_position():
	k


#-----events----------------
air.onclick(air_clicked)
wn = trtl.Screen()
wn.mainloop()