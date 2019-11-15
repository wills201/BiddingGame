bot = positions[0]
user = positions[10]
positions = [0,1,2,3,4,5,6,7,8,9,10]
actions = [0-100]
botmoney = 100
usermoney = 100
scotchpos = positions[5]
draw = user
#Alot of this is sudo code, just wanted to get my ideas on how I wanted to code the problem on the file.
def reward(state, action, position):
    if scotchpos == positions[5] and (botmoney > usermoney):
        #Reward goes here but im not sure how to code it lol
    
def makingmove(action):
    botmoney.action
    usermoney.action
    
#Checks who won the turn, also sees who has draw adv
def checkwin(action, scotchpos):
    if botmoney.action > usermoney.action:
        botmoney -= actions
        scotchpos - 1
    if usermoney.action > botmoney.action:
        usermoney -= actions
        scotchpos + 1
    if usermoney.actions == botmoney.actions:
        drawadv()

def drawadv():
    if draw == user:
        scotchpos + 1
        usermoney -= actions
        draw = bot
    if draw == bot:
        scotchpos - 1
        botmoney -= actions
        draw = user
    