# Title: Main L-System Drawing Script
# By: Mehmet Yilmaz

from tkinter import *
from turtle import *
import turtle
import re

def makeString(list):
    ans = ""
    for i in range(len(list)):
        ans = ans + list[i]
    return ans

def makeList(s):
    ans = []
    for i in range(len(s)):
        ans.append(str(s[i]))
    return ans

def getState(turtle):
    return turtle.heading(), turtle.position()

def restoreState(turtle, state):
    turtle.setheading(state[0])
    turtle.setposition(state[1][0], state[1][1])

def generate_path(n, variables, start, rules):
    for i in range(n):
        for p in range(len(variables)):
            v = variables[p]
            for z in range(len(start)):
                if(start[z] == v):
                    start[z] = rules[p]
        temp = makeString(start)
        start = makeList(temp)
    return start

def main(title, variables, moveForward, turnLeft, turnRight, start, rules, angle, n, dis, saveImage):
    turtle.reset()
    spd = 100000
    seeDrawing = False
    hideArrow = True

    start = generate_path(n, variables, start, rules)

    if(seeDrawing == False):
        speed(spd)
        turtle.tracer(0, 0)

    savedState = []
    stack = []

    poses = [turtle.pos()]

    for k in range(2):

        if(hideArrow):
            hideturtle()

        for i in range(len(start)):
            key = start[i]
            if(moveForward.count(key)):
                forward(dis)
            elif(turnLeft.count(key)):
                left(angle)
            elif(turnRight.count(key)):
                right(angle)
            elif(key == "["):
                savedState = getState(turtle)
                stack.append(savedState)
            elif(key == "]"):
                turtle.penup()
                restoreState(turtle, stack[-1])
                stack.pop()
                turtle.pendown()
            
            poses.append(turtle.pos())
        
        avg = [sum(x)/len(x)*(-1) for x in zip(*poses)]

        if(k == 0):
            turtle.reset()

            turtle.penup()
            turtle.goto(avg[0], avg[1])
            turtle.pendown()

    if(saveImage):
        title = re.sub("\s+", "_", title.strip()) + ".eps"
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file=str(title))

    if(seeDrawing == False):
        turtle.update()

    done()


