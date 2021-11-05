import random
from graphics import *
window=GraphWin('19290292',300,350)

#XOX game
#graphics.py is a prepared library


R1=Rectangle(Point(0,0),Point(100,100))
R2=Rectangle(Point(100,0),Point(200,100))
R3=Rectangle(Point(200,0),Point(300,100))
R4=Rectangle(Point(0,100),Point(100,200))
R5=Rectangle(Point(100,100),Point(200,200))
R6=Rectangle(Point(200,100),Point(300,200))
R7=Rectangle(Point(0,200),Point(100,300))
R8=Rectangle(Point(100,200),Point(200,300))
R9=Rectangle(Point(200,200),Point(300,300))

R1.draw(window)
R2.draw(window)
R3.draw(window)
R4.draw(window)
R5.draw(window)
R6.draw(window)
R7.draw(window)
R8.draw(window)
R9.draw(window)


write=Text(Point(150,320),'')
write.draw(window)
kare1,kare2,kare3,kare4,kare5,kare6,kare7,kare8,kare9=None,None,None,None,None,None,None,None,None
kareler=[R1,R2,R3,R4,R5,R6,R7,R8,R9]


def random0():
  global kare1, kare2, kare3, kare4, kare5, kare6, kare7, kare8, kare9
  global kareler
  a=random.choice(kareler)
  if a==R1:
      kareler.remove(a)
      Text(a.getCenter(), 'O').draw(window)
      kare1='O'

  elif a==R2:
      kareler.remove(a)
      Text(a.getCenter(), 'O').draw(window)
      kare2 = 'O'

  elif a==R3:
      kareler.remove(a)
      Text(a.getCenter(), 'O').draw(window)
      kare3 = 'O'

  elif a==R4:
      kareler.remove(a)
      Text(a.getCenter(), 'O').draw(window)
      kare4 = 'O'

  elif a==R5:
      kareler.remove(a)
      Text(a.getCenter(), 'O').draw(window)
      kare5 = 'O'

  elif a==R6:
      kareler.remove(a)
      Text(a.getCenter(), 'O').draw(window)
      kare6 = 'O'

  elif a==R7:
      kareler.remove(a)
      Text(a.getCenter(), 'O').draw(window)
      kare7 = 'O'

  elif a==R8:
      kareler.remove(a)
      Text(a.getCenter(), 'O').draw(window)
      kare8 = 'O'

  elif a==R9:
      kareler.remove(a)
      Text(a.getCenter(), 'O').draw(window)
      kare9 = 'O'

def Xkazanma():
    global kare1,kare2,kare3,kare4,kare5,kare6,kare7,kare8,kare9
    if kare1=='X' and kare2=='X' and kare3=='X':
        write.setText('X Wins')
    elif kare4=='X' and kare5=='X' and kare6=='X':
        write.setText('X Wins')
    elif kare7=='X' and kare8=='X' and kare9=='X':
        write.setText('X Wins')
    elif kare1=='X' and kare4=='X' and kare7=='X':
        write.setText('X Wins')
    elif kare2=='X' and kare5=='X' and kare8=='X':
        write.setText('X Wins')
    elif kare3=='X' and kare6=='X' and kare9=='X':
        write.setText('X Wins')
    elif kare1=='X' and kare5=='X' and kare9=='X':
        write.setText('X Wins')
    elif kare3=='X' and kare5=='X' and kare7=='X':
        write.setText('X Wins')

def Okazanma():
    global kare1, kare2, kare3, kare4, kare5, kare6, kare7, kare8, kare9
    if kare1=='O' and kare2=='O' and kare3=='O':
        write.setText('O Wins')
    elif kare4=='O' and kare5=='O' and kare6=='O':
        write.setText('O Wins')
    elif kare7=='O' and kare8=='O' and kare9=='O':
        write.setText('O Wins')
    elif kare1=='O' and kare4=='O' and kare7=='O':
        write.setText('O Wins')
    elif kare2=='O' and kare5=='O' and kare8=='O':
        write.setText('O Wins')
    elif kare3=='O' and kare6=='O' and kare9=='O':
        write.setText('O Wins')
    elif kare1=='O' and kare5=='O' and kare9=='O':
        write.setText('O Wins')
    elif kare3=='O' and kare5=='O' and kare7=='O':
        write.setText('O Wins')

key=''
key2=''
try:
 while True:
    point=window.getMouse()
    xpoint=point.getX()
    ypoint=point.getY()

    if 0<xpoint<100 and 0<ypoint<100:     #R1
        try:
         kareler.remove(R1)
         Text(R1.getCenter(), 'X').draw(window)
         kare1='X'
         if len(kareler)!=0:
          random0()
        except ValueError:
            write.setText('You cannot click the filled squares')

    elif 100<xpoint<200 and 0<ypoint<100: #r2
        try:
          kareler.remove(R2)
          Text(R2.getCenter(), 'X').draw(window)
          kare2='X'
          if len(kareler) != 0:
           random0()
        except ValueError:
            write.setText('You cannot click the filled squares')
    elif 200<xpoint<300 and 0<ypoint<100: #r3
        try:
          kareler.remove(R3)
          Text(R3.getCenter(), 'X').draw(window)
          kare3='X'
          if len(kareler) != 0:
           random0()
        except ValueError:
            write.setText('You cannot click the filled squares')

    elif 0<xpoint<100 and 100<ypoint<200: #R4
        try:
          kareler.remove(R4)
          Text(R4.getCenter(), 'X').draw(window)
          kare4='X'
          if len(kareler) != 0:
           random0()
        except ValueError:
            write.setText('You cannot click the filled squares')

    elif 100<xpoint<200 and 100<ypoint<200: #R5
        try:
          kareler.remove(R5)
          Text(R5.getCenter(), 'X').draw(window)
          kare5='X'
          if len(kareler) != 0:
           random0()
        except ValueError:
            write.setText('You cannot click the filled squares')

    elif 200<xpoint<300 and 100<ypoint<200: #R6
        try:
          kareler.remove(R6)
          Text(R6.getCenter(), 'X').draw(window)
          kare6='X'
          if len(kareler) != 0:
           random0()
        except ValueError:
            write.setText('You cannot click the filled squares')

    elif 0<xpoint<100 and 200<ypoint<300: #R7
        try:
          kareler.remove(R7)
          Text(R7.getCenter(), 'X').draw(window)
          kare7='X'
          if len(kareler) != 0:
           random0()
        except ValueError:
            write.setText('You cannot click the filled squares')

    elif 100<xpoint<200 and 200<ypoint<300: #R8
        try:
          kareler.remove(R8)
          Text(R8.getCenter(), 'X').draw(window)
          kare8='X'
          if len(kareler) != 0:
           random0()
        except ValueError:
            write.setText('You cannot click the filled squares')

    elif 200<xpoint<300 and 200<ypoint<300:   #R9
        try:
          kareler.remove(R9)
          Text(R9.getCenter(),'X').draw(window)
          kare9='X'
          if len(kareler) != 0:
           random0()
        except ValueError:
                write.setText('You cannot click the filled squares')

    Xkazanma()

    if write.getText()=='X Wins':
       while True:
        key = window.getKey()
        if key == 'q':
            window.close()

    Okazanma()

    if write.getText()=='O Wins':
      while True:
        key = window.getKey()
        if key == 'q':
            window.close()

    if len(kareler)==0:
      write.setText('Draw!')
      while True:
        key2 = window.getKey()
        if key2 == 'q':
            window.close()
except:
   pass
