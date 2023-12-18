
import time
from sense_hat import SenseHat
sense = SenseHat()

#all sensehat graphics should be here.

B = (0,0,255)
G = (0, 255, 0)
R = (255, 0, 0)
D = (155, 0, 0)
P = (55, 0, 0)
O = (255,155,0)
Y = (255,255,0)
X = (0,0,0)

initGraphic1 = [
R, X, X, X, X, X, X, Y,
X, X, X, X, X, X, X, X,
X, X, D, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
G, X, X, X, X, X, X, B,

]

initGraphic2 = [
R, R, X, X, X, X, X, Y,
X, R, X, X, X, X, Y, Y,
X, X, D, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
G, G, X, X, X, X, B, X,
G, X, X, X, X, X, B, B,

]

initGraphic3 = [
R, R, R, X, X, X, X, Y,
X, R, R, X, X, X, Y, Y,
X, X, R, X, X, Y, Y, Y,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
G, G, G, X, X, B, X, X,
G, G, X, X, X, B, B, X,
G, X, X, X, X, B, B, B,

]

initGraphic4 = [
R, R, R, R, X, X, X, Y,
X, R, R, R, X, X, Y, Y,
X, X, R, R, X, Y, Y, Y,
X, X, X, R, Y, Y, Y, Y,
G, G, G, G, B, X, X, X,
G, G, G, X, B, B, X, X,
G, G, X, X, B, B, B, X,
G, X, X, X, B, B, B, B,

]

initGraphic5 = [
R, R, R, R, R, X, X, Y,
X, R, R, R, R, X, Y, Y,
X, X, R, R, R, Y, Y, Y,
G, G, G, R, Y, Y, Y, Y,
G, G, G, G, B, Y, Y, Y,
G, G, G, B, B, B, X, X,
G, G, X, B, B, B, B, X,
G, X, X, B, B, B, B, B,

]

initGraphic6 = [
R, R, R, R, R, R, X, Y,
X, R, R, R, R, R, Y, Y,
G, G, R, R, R, Y, Y, Y,
G, G, G, R, Y, Y, Y, Y,
G, G, G, G, B, Y, Y, Y,
G, G, G, B, B, B, Y, Y,
G, G, B, B, B, B, B, X,
G, X, B, B, B, B, B, B,

]

initGraphic7 = [
R, R, R, R, R, R, R, Y,
G, R, R, R, R, R, Y, Y,
G, G, R, R, R, Y, Y, Y,
G, G, G, R, Y, Y, Y, Y,
G, G, G, G, B, Y, Y, Y,
G, G, G, B, B, B, Y, Y,
G, G, B, B, B, B, B, Y,
G, B, B, B, B, B, B, B,

]

rightGraphic = [

X, X, X, X, X, P, D, R,
X, X, X, X, X, P, D, R,
X, X, X, X, X, P, D, R,
X, X, X, X, X, P, D, R,
X, X, X, X, X, P, D, R,
X, X, X, X, X, P, D, R,
X, X, X, X, X, P, D, R,
X, X, X, X, X, P, D, R,

]

leftGraphic = [

R, D, P, X, X, X, X, X,
R, D, P, X, X, X, X, X,
R, D, P, X, X, X, X, X,
R, D, P, X, X, X, X, X,
R, D, P, X, X, X, X, X,
R, D, P, X, X, X, X, X,
R, D, P, X, X, X, X, X,
R, D, P, X, X, X, X, X,
]

bothGraphic = [

R, D, P, X, X, P, D, R,
R, D, P, X, X, P, D, R,
R, D, P, X, X, P, D, R,
R, D, P, X, X, P, D, R,
R, D, P, X, X, P, D, R,
R, D, P, X, X, P, D, R,
R, D, P, X, X, P, D, R,
R, D, P, X, X, P, D, R,

]

inGraphic = [

X, X, X, X, G, X, X, X,
X, X, X, G, G, X, X, X,
X, X, G, G, G, X, X, X,
X, G, G, G, G, X, X, X,
X, G, G, G, G, X, X, X,
X, X, G, G, G, X, X, X,
X, X, X, G, G, X, X, X,
X, X, X, X, G, X, X, X,

]

outGraphic = [

X, X, X, R, X, X, X, X,
X, X, X, R, R, X, X, X,
X, X, X, R, R, R, X, X,
X, X, X, R, R, R, R, X,
X, X, X, R, R, R, R, X,
X, X, X, R, R, R, X, X,
X, X, X, R, R, X, X, X,
X, X, X, R, X, X, X, X,
]

smiley_face = [
X, X, X, X, X, X, X, X,
X, X, Y, X, Y, X, X, X,
X, X, Y, X, Y, X, X, X,
X, X, Y, X, Y, X, X, X,
Y, X, X, X, X, X, Y, X,
X, Y, X, X, X, Y, X, X,
X, X, Y, Y, Y, X, X, X,
X, X, X, X, X, X, X, X,
]

sad_face = [
X, X, X, X, X, X, X, X,
X, X, R, X, R, X, X, X,
X, X, R, X, R, X, X, X,
X, X, R, X, R, X, X, X,
X, X, X, X, X, X, X, X,
X, X, R, R, R, X, X, X,
X, R, X, X, X, R, X, X,
R, X, X, X, X, X, R, X,
]




def showScreen (graphic):	
	sense.set_pixels(graphic)
	return




















