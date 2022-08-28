#Universidad del Valle de Guatemala 
#Gráficos por computador 
#Gabriela Paola Contreras Guerra 20213

from gl import Renderer, color, V3, V2
from texture import Texture
import shader as s 
import math as m 

w = 700
h = 600

rend = Renderer(w, h)
#Medium
rend.glLookAt(V3(2,5,-3),V3(0,7.9,1))




#MAIN
position = V3(2,5,-3)
rend.active_shader = s.rainbow
rend.active_texture = Texture("model/earthDay.bmp")

rend.glLoadModel("model/coffee.obj",
                  translate = position,
                  rotate = V3(0, 70 , 0),
                  scale = V3(2, 2, 2))

position1 = V3(2.7,5,-2)
rend.active_shader = s.zebra


rend.glLoadModel("model/coffee.obj",
                  translate = position1,
                  rotate = V3(0, 0, 0),
                  scale = V3(2, 2, 2))

position2 = V3(0.8,5,-3)
rend.active_shader = s.degraded


rend.glLoadModel("model/coffee.obj",
                  translate = position2,
                  rotate = V3(0, 0, 0),
                  scale = V3(2, 2, 2))

rend.glFinish("output.bmp")

