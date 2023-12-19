import time
from graphics import *

#These functions show images from graphics.py using showScreen(graphicName)

def initAnimation():
	showScreen(initGraphic1)
	time.sleep(0.10)
	showScreen(initGraphic2)
	time.sleep(0.10)
	showScreen(initGraphic3)
	time.sleep(0.10)
	showScreen(initGraphic4)
	time.sleep(0.10)
	showScreen(initGraphic5)
	time.sleep(0.10)
	showScreen(initGraphic6)
	time.sleep(0.10)
	showScreen(initGraphic7)
	time.sleep(0.10)
	showScreen(initGraphic8)
	time.sleep(0.10)
	
def movementLeft():
	showScreen(leftGraphic)

def movementRight():
	showScreen(rightGraphic)

def movementBoth():
	showScreen(bothGraphic)

def movementIn():
	showScreen(inGraphic)
	
def movementOut():
	showScreen(outGraphic)

def smiley():
	showScreen(smiley_face)
	
def dead():
	showScreen(sad_face)

def cancel():
	showScreen(red_x)
