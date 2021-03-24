import turtle
import time


def drawGap():
    turtle.penup()
    turtle.forward(5)


def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    # turtle.pencolor(color)
    turtle.fd(40)
    drawGap()
    turtle.right(90)


def drawDigit(digit):
    turtle.penup()
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.right(180)
    turtle.penup()
    turtle.fd(20)


def drawDate(date):
    for i in date:
        if i == '-':
            turtle.write('年', font=("Arial", 35, "normal"))
            turtle.forward(60)
        elif i == '=':
            turtle.write('月', font=("Arial", 35, "normal"))
            turtle.forward(60)
        elif i == '+':
            turtle.write('日', font=("Arial", 35, "normal"))
            turtle.forward(60)
        elif i == ' ':
            turtle.forward(40)
        elif i == ':':
            turtle.write(':', font=("Arial", 35, "normal"))
            turtle.forward(20)
        else:
            drawDigit(eval(i))


def main():
    turtle.setup(1600, 350, 200, 200)
    turtle.penup()
    turtle.forward(-600)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+ %H:%M:%S', time.localtime()))
    turtle.done()


main()
