import cf
import turtle

mode = int(input('mode(1,2,3,4): '))
sacle = int(input('Scale: ')) // 2
iter = int(input('Iterations: '))


wn = turtle.Screen()
wn.colormode(255)
turtle.tracer(0, 0)
com = turtle.Turtle()
com.speed(0)
com.hideturtle()


for x in range(-2 * sacle, 2 * sacle) :
    for y in range(-2 * sacle, 2 * sacle) :
        z = cf.I(x/sacle,y/sacle)
        z1 = cf.I(x/sacle,y/sacle)
        for i in range(0, iter) :
            z1 = cf.sqr(z1)
            z1 = cf.add(z1,z)
            m = cf.mod(z1)
            if m > 2 :
                break
        if mode == 1 :
            #Coloured based on how long the iterates stay less than two(darker is longer)
            com.penup()
            com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
            com.pendown()
            hue = int(255 - 255 * i / iter)
            if hue != 255 :
                com.dot(3, (hue,255,255))
        if mode == 2 :
            #Colored based on the size of the norm after a number of iteration(Darker is larger)
            if m <= 2 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                hue = int(255 - 255 * m / 2)
                if hue != 255 :
                    com.dot(3, (hue,255,255))
        if mode == 3 :
            #Colored in black and white
            if m <= 2 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'black')
        if mode == 4 :
            #Coloured based on the relative size of the norm(Darker is larger) 
            if m <= 0.2 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'pale turquoise')
            elif m <= 0.4 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'sky blue')
            elif m <= 0.6 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'cyan2')
            elif m <= 0.8 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'aquamarine')
            elif m <= 1 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'aquamarine2')
            elif m <= 1.2 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'SeaGreen1')
            elif m <= 1.4 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'SeaGreen2')
            elif m <= 1.6 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'SeaGreen3')
            elif m <= 1.8 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'medium sea green')
            elif m < 2 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'sea green')
    turtle.update()

import cf
import turtle

mode = int(input('mode(1,2,3,4): '))
sacle = int(input('Scale: ')) // 2
iter = int(input('Iterations: '))


wn = turtle.Screen()
wn.colormode(255)
turtle.tracer(0, 0)
com = turtle.Turtle()
com.speed(0)
com.hideturtle()


for x in range(-2 * sacle, 2 * sacle) :
    for y in range(-2 * sacle, 2 * sacle) :
        z = cf.I(x/sacle,y/sacle)
        z1 = cf.I(x/sacle,y/sacle)
        for i in range(0, iter) :
            z1 = cf.sqr(z1)
            z1 = cf.add(z1,z)
            m = cf.mod(z1)
            if m > 2 :
                break
        if mode == 1 :
            #Coloured based on how long the iterates stay less than two(darker is longer)
            com.penup()
            com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
            com.pendown()
            hue = int(255 - 255 * i / iter)
            if hue != 255 :
                com.dot(3, (hue,255,255))
        if mode == 2 :
            #Colored based on the size of the norm after a number of iteration(Darker is larger)
            if m <= 2 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                hue = int(255 - 255 * m / 2)
                if hue != 255 :
                    com.dot(3, (hue,255,255))
        if mode == 3 :
            #Colored in black and white
            if m <= 2 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'black')
        if mode == 4 :
            #Coloured based on the relative size of the norm(Darker is larger) 
            if m <= 0.2 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'pale turquoise')
            elif m <= 0.4 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'sky blue')
            elif m <= 0.6 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'cyan2')
            elif m <= 0.8 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'aquamarine')
            elif m <= 1 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'aquamarine2')
            elif m <= 1.2 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'SeaGreen1')
            elif m <= 1.4 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'SeaGreen2')
            elif m <= 1.6 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'SeaGreen3')
            elif m <= 1.8 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'medium sea green')
            elif m < 2 :
                com.penup()
                com.setpos(cf.Re(z) * sacle,cf.Im(z) * sacle)
                com.pendown()
                com.dot(3, 'sea green')
    turtle.update()

