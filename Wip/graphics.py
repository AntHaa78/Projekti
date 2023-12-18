
import time
from sense_hat import SenseHat
sense = SenseHat()

#all sensehat graphics should be here.

B = (0,0,255)
G = (0, 255, 0)
R = (255, 0, 0)
R1 = (220, 40, 0)
R2 = (185, 80, 0)
R3 = (150, 115, 0)
R4 = (115, 150, 0)
R5 = (80, 185, 0)
R6 = (40, 220, 0)
D1 = (170, 0, 0)
D2 = (85, 0, 0)
P = (55, 0, 0)
O = (255,155,0)
Y = (255,255,0)
X = (0,0,0)

initGraphic1 = [
R, X, X, X, X, X, X, X,
R, X, X, X, X, X, X, X,
R, X, X, X, X, X, X, X,
R, X, X, X, X, X, X, X,
R, X, X, X, X, X, X, X,
R, X, X, X, X, X, X, X,
R, X, X, X, X, X, X, X,
R, X, X, X, X, X, X, X,

]

initGraphic2 = [
R, R1, X, X, X, X, X, X,
R, R1, X, X, X, X, X, X,
R, R1, X, X, X, X, X, X,
R, R1, X, X, X, X, X, X,
R, R1, X, X, X, X, X, X,
R, R1, X, X, X, X, X, X,
R, R1, X, X, X, X, X, X,
R, R1, X, X, X, X, X, X,

]

initGraphic3 = [
R, R1, R2, X, X, X, X, X,
R, R1, R2, X, X, X, X, X,
R, R1, R2, X, X, X, X, X,
R, R1, R2, X, X, X, X, X,
R, R1, R2, X, X, X, X, X,
R, R1, R2, X, X, X, X, X,
R, R1, R2, X, X, X, X, X,
R, R1, R2, X, X, X, X, X,

]

initGraphic4 = [
R, R1, R2, R3, X, X, X, X,
R, R1, R2, R3, X, X, X, X,
R, R1, R2, R3, X, X, X, X,
R, R1, R2, R3, X, X, X, X,
R, R1, R2, R3, X, X, X, X,
R, R1, R2, R3, X, X, X, X,
R, R1, R2, R3, X, X, X, X,
R, R1, R2, R3, X, X, X, X,

]

initGraphic5 = [
R, R1, R2, R3, R4, X, X, X,
R, R1, R2, R3, R4, X, X, X,
R, R1, R2, R3, R4, X, X, X,
R, R1, R2, R3, R4, X, X, X,
R, R1, R2, R3, R4, X, X, X,
R, R1, R2, R3, R4, X, X, X,
R, R1, R2, R3, R4, X, X, X,
R, R1, R2, R3, R4, X, X, X,

]

initGraphic6 = [
R, R1, R2, R3, R4, R5, X, X,
R, R1, R2, R3, R4, R5, X, X,
R, R1, R2, R3, R4, R5, X, X,
R, R1, R2, R3, R4, R5, X, X,
R, R1, R2, R3, R4, R5, X, X,
R, R1, R2, R3, R4, R5, X, X,
R, R1, R2, R3, R4, R5, X, X,
R, R1, R2, R3, R4, R5, X, X,

]

initGraphic7 = [
R, R1, R2, R3, R4, R5, R6, X,
R, R1, R2, R3, R4, R5, R6, X,
R, R1, R2, R3, R4, R5, R6, X,
R, R1, R2, R3, R4, R5, R6, X,
R, R1, R2, R3, R4, R5, R6, X,
R, R1, R2, R3, R4, R5, R6, X,
R, R1, R2, R3, R4, R5, R6, X,
R, R1, R2, R3, R4, R5, R6, X,

]

initGraphic8 = [
R, R1, R2, R3, R4, R5, R6, G,
R, R1, R2, R3, R4, R5, R6, G,
R, R1, R2, R3, R4, R5, R6, G,
R, R1, R2, R3, R4, R5, R6, G,
R, R1, R2, R3, R4, R5, R6, G,
R, R1, R2, R3, R4, R5, R6, G,
R, R1, R2, R3, R4, R5, R6, G,
R, R1, R2, R3, R4, R5, R6, G,

]

rightGraphic = [

X, X, X, X, X, D2, D1, R,
X, X, X, X, X, D2, D1, R,
X, X, X, X, X, D2, D1, R,
X, X, X, X, X, D2, D1, R,
X, X, X, X, X, D2, D1, R,
X, X, X, X, X, D2, D1, R,
X, X, X, X, X, D2, D1, R,
X, X, X, X, X, D2, D1, R,

]

leftGraphic = [

R, D1, D2, X, X, X, X, X,
R, D1, D2, X, X, X, X, X,
R, D1, D2, X, X, X, X, X,
R, D1, D2, X, X, X, X, X,
R, D1, D2, X, X, X, X, X,
R, D1, D2, X, X, X, X, X,
R, D1, D2, X, X, X, X, X,
R, D1, D2, X, X, X, X, X,
]

bothGraphic = [

R, D1, D2, X, X, D2, D1, R,
R, D1, D2, X, X, D2, D1, R,
R, D1, D2, X, X, D2, D1, R,
R, D1, D2, X, X, D2, D1, R,
R, D1, D2, X, X, D2, D1, R,
R, D1, D2, X, X, D2, D1, R,
R, D1, D2, X, X, D2, D1, R,
R, D1, D2, X, X, D2, D1, R,

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




















