#simple GUI
#import motion
import time

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "nico.d.mtholyoke.edu", 9559)

from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Simple GUI")
#sets the width/height of window
root.geometry("200x200")

#button for saying hello
def sayHello():
	print "Nico says hello!"
	#tts.say("Hi, my name is Neeko!")


bHello = Button(root, text="Say Hello!",command=sayHello)
bHello.pack()

#button for introduction
def greet():
	print "Say hi"
	#tts.say("Hey Nicole!")

#button to greet
bIntroduce = Button(root, text="Greet",command=greet)
bIntroduce.pack()

def armsUp():
	print "Raise arms"
	#main("nico.d.mtholyoke.edu", 9559)

#button to call movement
bMove = Button(root, text="Arms up",command=armsUp)
bMove.pack()

#function that holds a movement
def main(robotIP, PORT = 9559):
	postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

	#postureProxy.goToPosture("Sit",5.0)
	postureProxy.goToPosture("StandZero",5.0)

#kick off the event loop
root.mainloop()
