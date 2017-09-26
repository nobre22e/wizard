#import adialog_new as ad
from naoqi import ALProxy
import nicoGestures as gesture
import sys

try:
	tts = ALProxy("ALTextToSpeech", "nico.d.mtholyoke.edu", 9559)
except Exception,e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ",e
	sys.exit(1)

dialog = {
	######## Introduction ########
	'1': "Hello! My name is Neeco. How are you doing today?" ,
	'2': "I'm ready to learn mahth! Do you have any problems for me to solve?",
	'3': "What problems are we solving today?",
	'4': "I want to learn how to solve this problem!",
	######## Confirmation ########
	'5': "Okay!",
	'6': "Yes!",
	'7': "Yes, I agree.",
	######## Asking Questions #######
	'8': "How do you solve this problem?",
	'9': "What do we do next?",
	'10': "How do we do that?",
	'28': "How should we start?",
	'11': "Could you give me more information?",
	'12': "Okay now we mul tip ly?",
	'13': "Okay now we subtract?",
	'14': "Okay so we divide?",
	'15': "Is this correct?",
	######## Confusion ########
	'16': "How did we get that number?",
	'17': "Could you break that down into parts?",
	'18': "Hmmm. That part seems complicated to me. Can you explain that again?",
	'19': "I don't know. Could you give me some hints?",
	######## Ending/Understanding ########
	'20': "I think I understand now.",
	'21': "I think this is correct.",
	'22': "Yay, we solved the problem!",
	'23': "Thank you! You're awesome. You made me feel smarter.",
	'24': "I'm getting tired now, but I think I understand the problem better. Maybe we can continue this another time.",
	######## What We Know #######
	'25': "I know that 1 fluid ounce of paint will cover 3 square inches of my body.",
	'26': "I know that I can drive 60 miles in 1 hour.",
	'27': "I know that I can swim 5 feet per second and that the tide is coming in at 2 feet per second.",
	'29': "Please tap the, next, button for me so we can go on to the next step.",
	######## Survey Questions ########
	'30': "Do you like mahth?",
	'31': "Have you done problems like these before?",
	'32': "Was it hard when you first started?"
}

# If the 
def speak(command_dialog):
	if command_dialog.isdigit() and (int(command_dialog) <= 32):
		tts.post.say(dialog[command_dialog])
	else:
		tts.say(command_dialog)
	
#Hello
def hello(command_dialog):
	gesture.waveRight2()
	tts.say(dialog[command_dialog])

def shrugAndShakeHead(command_dialog):
	gesture.shrug_and_shakehead()
	speak(command_dialog)

#nodding yes
def nod(command_dialog):
    gesture.nodYes()
    speak(command_dialog)

def fistYay(command_dialog):
	gesture.fistYay()
	speak(command_dialog)

#shaking no
def shakeHead(command_dialog):
	gesture.shakeNo()
	speak(command_dialog)

def handsHips(command_dialog):
	gesture.handsOnHips()
	speak(command_dialog)

def handOutLeft(command_dialog):
	gesture.handOutLeft()
	speak(command_dialog)

def handOutRight(command_dialog):
	gesture.handOutRight()
	speak(command_dialog)

def handChestLeft(command_dialog):
	gesture.handOnChestLeft()
	speak(command_dialog)

def bigShrug(command_dialog):
	gesture.largeShrug()
	speak(command_dialog)

def handLookAndOut(command_dialog):
	gesture.lookAtNailsRight()
	speak(command_dialog)
	gesture.handOutRight2()

def cheer(command_dialog):
	gesture.cheering()
	speak(command_dialog)

# Control what to do for built in commands or entered speech
def sendCmd(inp):
	if inp == '0':
		gesture.faceForward()
	elif inp == '1':
		hello(inp)
	elif inp in {'2', '3'} or inp[0:6].lower() == "i will" or inp[0:6].lower() == "i need" or inp[0:7].lower() == "it will":
		handsHips(inp)
	elif inp == '4':
		handChestLeft(inp)
	elif inp in {'5', '6', '7', '12', '13', '14', '20'}:
		nod(inp)
	elif inp in {'8', '9'}:
		bigShrug(inp)
	elif inp in {'10', '16', '20', '21', '28','30','32'} or inp[0:2].lower() == "we" or inp[0:2].lower() == "do":
		handOutLeft(inp)
	elif inp in {'11', '15', '17', '25', '26', '27', '29','31'} or inp[0:10].lower() == "the answer":
		handOutRight(inp)
	elif inp == '18':
		handLookAndOut(inp)
	elif inp == '19':
		shrugAndShakeHead(inp)
	elif inp == '23':
		fistYay(inp)
	elif inp == '22':
		cheer(inp)
	elif inp == '24':
		shakeHead(inp)
	elif inp == '33':
		gesture.turnHeadLeft()
	elif inp == '34':
		gesture.turnHeadRight()
	elif inp == '35':
		gesture.nodYes()
	else:
		speak(inp)
