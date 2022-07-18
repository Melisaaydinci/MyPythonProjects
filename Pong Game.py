"""
Created by Zeynep ÖZDEMİR, ÖZGE MERCANOĞLU SİNCAN
"""
from graphics import *
import random
import math



# Do not change these following 4 variables
margin = 10  # height of the paddle from the ground
moveIncrement = 15  # paddle movement
ballRadius = 15
BOUNCE_WAIT = 1200


BALL_COUNT = 1  # If we change this, the number of ball changes!


class Timer:
    def __init__(self):
        self.value = 0


class Paddle:  #myPaddle = Paddle("White", 100, 15, 150, win)

    def __init__(self, color, width, height, coordx, win):
        self.color = color
        self.width = width
        self.height = height
        self.x = coordx
        self.shape = Rectangle(Point(self.x - int(self.width / 2), win.getHeight() - margin - self.height),
                               Point(self.x + int(self.width / 2), win.getHeight() - margin))
        self.shape.setFill(self.color)
        self.window = win
        self.shape.draw(self.window)

    def move_left(self):  # move paddle to the left by the amount of global variable moveIncrement
        if 50<=self.x:
          self.x -= moveIncrement
          self.shape.move(-moveIncrement, 0)

    def move_right(self):  # move paddle to the right by the amount of global variable moveIncrement
        if self.x<250:
          self.x += moveIncrement
          self.shape.move(moveIncrement, 0)


# TODO
#class Bubbles:
# Define it by yourself to implement bubbles in the assignment
class Bubbles:
    def __init__(self,xcord,ycord,color2,win):
       self.circle=Circle(Point(xcord,ycord),30)
       self.xcord=xcord
       self.ycord=ycord
       self.color2=color2
       self.wind=win
       self.circle.setFill(self.color2)
       self.circle.draw(self.wind)

class Ball:

    def __init__(self, coordx, coordy, color, radius, x_direction, speed, win):
        self.shape = Circle(Point(coordx, coordy), radius)
        self.x = coordx
        self.y = coordy
        self.xMovement = 0  # Current x movement
        self.yMovement = 0  # Current y movement
        self.color = color
        self.window = win
        self.shape.setFill(self.color)
        self.shape.draw(self.window)
        self.radius = radius
        self.timer = 0
        self.x_direction = x_direction  # Initial x direction. This variable will be 0 or 1. 1:right 0:left
        self.speed = speed

    def is_moving(self):
        if self.xMovement!=0 and self.yMovement!=0:
            return True
        return False

    def bounce(self, gameTimer, minX, maxX, maxY):
        # Calculating x-axis ball movement and bouncing
        # minX: min x coord. of paddle
        # maxX: max x coord. of paddle
        # maxY: max y coord. at which the ball can be move. If it goes further, it falls to the ground.

        global BOUNCE_WAIT
        gameOver = False

        if gameTimer >= self.timer + BOUNCE_WAIT:
              self.timer = gameTimer

              if self.x <= 15:
                  self.xMovement = 1
              if self.x >= 285:
                  self.xMovement = -1
              if self.y <= 15:
                  self.yMovement = 1

              if self.xMovement!=0:
                 if maxY>self.y>=maxY-15 and minX+5<self.x<maxX+5:
                    self.yMovement=-1
                 if self.y>maxY+10:
                      gameOver=True

              if self.yMovement == -1:
                  self.y -= self.speed
              elif self.yMovement == 1:
                  self.y += self.speed

              if self.xMovement == 1:
                  self.x += self.speed

              elif self.xMovement == -1:
                  self.x -= self.speed

              self.shape.move(self.xMovement * self.speed, self.yMovement * self.speed)
              return gameOver



def main():

   win = GraphWin("19290292 Pong Game", 300, 600)  # Replace your student id
   lives = 2
   win.setBackground("Black")
   ColorsList = ["Cyan", "Red", "Green", "Yellow"]
   while True:
       if lives!=0:
         myPaddle = Paddle("White", 100, 15, 150, win)
       BallList = list()
       BubblesList = list()
       ALLBubblesList = list()

       def is_touch(topunxdegeri, topunydegeri):

           if 0 < topunxdegeri < 60 and 0 < topunydegeri < 60:
               if bubbles1 not in BubblesList:
                   BubblesList.append(bubbles1)
               bubbles1.circle.undraw()

           if 60 < topunxdegeri < 120 and 0 < topunydegeri < 60:
               if bubbles2 not in BubblesList:
                   BubblesList.append(bubbles2)
               bubbles2.circle.undraw()

           if 120 < topunxdegeri < 180 and 0 < topunydegeri < 60:
               if bubbles3 not in BubblesList:
                   BubblesList.append(bubbles3)
               bubbles3.circle.undraw()

           if 180 < topunxdegeri < 240 and 0 < topunydegeri < 60:
               if bubbles4 not in BubblesList:
                   BubblesList.append(bubbles4)
               bubbles4.circle.undraw()

           if 240 < topunxdegeri < 300 and 0 < topunydegeri < 60:
               if bubbles5 not in BubblesList:
                   BubblesList.append(bubbles5)
               bubbles5.circle.undraw()

           if 0 < topunxdegeri < 60 and 60 < topunydegeri < 120:
               if bubbles6 not in BubblesList:
                   BubblesList.append(bubbles6)
               bubbles6.circle.undraw()

           if 60 < topunxdegeri < 120 and 60 < topunydegeri < 120:
               if bubbles7 not in BubblesList:
                   BubblesList.append(bubbles7)
               bubbles7.circle.undraw()

           if 120 < topunxdegeri < 180 and 60 < topunydegeri < 120:
               if bubbles8 not in BubblesList:
                   BubblesList.append(bubbles8)
               bubbles8.circle.undraw()

           if 180 < topunxdegeri < 240 and 60 < topunydegeri < 120:
               if bubbles9 not in BubblesList:
                   BubblesList.append(bubbles9)
               bubbles9.circle.undraw()

           if 240 < topunxdegeri < 300 and 60 < topunydegeri < 120:
               if bubbles10 not in BubblesList:
                   BubblesList.append(bubbles10)
               bubbles10.circle.undraw()

           if 0 < topunxdegeri < 60 and 120 < topunydegeri < 180:
               if bubbles11 not in BubblesList:
                   BubblesList.append(bubbles11)
               bubbles11.circle.undraw()

           if 60 < topunxdegeri < 120 and 120 < topunydegeri < 180:
               if bubbles12 not in BubblesList:
                   BubblesList.append(bubbles12)
               bubbles12.circle.undraw()

           if 120 < topunxdegeri < 180 and 120 < topunydegeri < 180:
               if bubbles13 not in BubblesList:
                   BubblesList.append(bubbles13)
               bubbles13.circle.undraw()

           if 180 < topunxdegeri < 240 and 120 < topunydegeri < 180:
               if bubbles14 not in BubblesList:
                   BubblesList.append(bubbles14)
               bubbles14.circle.undraw()

           if 240 < topunxdegeri < 300 and 120 < topunydegeri < 180:
               if bubbles15 not in BubblesList:
                   BubblesList.append(bubbles15)
               bubbles15.circle.undraw()


       if lives!=0:
        bubbles1 = Bubbles(30, 30, 'red', win)

        bubbles2 = Bubbles(90, 30, 'red', win)

        bubbles3 = Bubbles(150, 30, 'red', win)

        bubbles4 = Bubbles(210, 30, 'red', win)

        bubbles5 = Bubbles(270, 30, 'red', win)

        bubbles6 = Bubbles(30, 90, 'yellow', win)

        bubbles7 = Bubbles(90, 90, 'yellow', win)

        bubbles8 = Bubbles(150, 90, 'yellow', win)

        bubbles9 = Bubbles(210, 90, 'yellow', win)

        bubbles10 = Bubbles(270, 90, 'yellow', win)

        bubbles11 = Bubbles(30, 150, 'blue', win)

        bubbles12 = Bubbles(90, 150, 'blue', win)

        bubbles13 = Bubbles(150, 150, 'blue', win)

        bubbles14 = Bubbles(210, 150, 'blue', win)

        bubbles15 = Bubbles(270, 150, 'blue', win)

       if bubbles1 not in ALLBubblesList:
           ALLBubblesList.append(bubbles1)
       if bubbles2 not in ALLBubblesList:
           ALLBubblesList.append(bubbles2)
       if bubbles3 not in ALLBubblesList:
           ALLBubblesList.append(bubbles3)
       if bubbles4 not in ALLBubblesList:
           ALLBubblesList.append(bubbles4)
       if bubbles5 not in ALLBubblesList:
           ALLBubblesList.append(bubbles5)
       if bubbles6 not in ALLBubblesList:
           ALLBubblesList.append(bubbles6)
       if bubbles7 not in ALLBubblesList:
           ALLBubblesList.append(bubbles7)
       if bubbles8 not in ALLBubblesList:
           ALLBubblesList.append(bubbles8)
       if bubbles9 not in ALLBubblesList:
           ALLBubblesList.append(bubbles9)
       if bubbles10 not in ALLBubblesList:
           ALLBubblesList.append(bubbles10)
       if bubbles11 not in ALLBubblesList:
           ALLBubblesList.append(bubbles11)
       if bubbles12 not in ALLBubblesList:
           ALLBubblesList.append(bubbles12)
       if bubbles13 not in ALLBubblesList:
           ALLBubblesList.append(bubbles13)
       if bubbles14 not in ALLBubblesList:
           ALLBubblesList.append(bubbles14)
       if bubbles15 not in ALLBubblesList:
           ALLBubblesList.append(bubbles15)

       for i in range(BALL_COUNT):
        rand_speed = random.randint(3, 5)  # random speed for ball
        # Note that the speed of the balls may vary depending on the hardware. If it is too fast or too slow, you can change the speed range for yourself while testing.
        # However, if you change these range, do not forget to reset these values to the initial limits before sending us.

        rand_direction = random.randint(0, 1)  # This variable will be 0 or 1 randomly.
        if lives!=0:
         ball = Ball(myPaddle.x - int(myPaddle.width / 2) + i * 30,
                    win.getHeight() - margin - myPaddle.height - ballRadius, ColorsList[i % 4], ballRadius,
                    rand_direction, rand_speed, win)
        BallList.append(ball)



        livesCounter = Text(Point(win.getWidth() - int(win.getWidth() / 5), 250), f'Lives -- {lives}')
        livesCounter.setTextColor("Cyan")
        livesCounter.setSize(15)
        livesCounter.draw(win)
       gameTimer = Timer()

       gameOver = False

       while lives > 0:
         while not gameOver:
            keyPress = win.checkKey()
            if keyPress == 'a':
                myPaddle.move_left()

            if keyPress == 'd':
                myPaddle.move_right()

            if keyPress == 'l':  # balls will move faster
                for item in BallList:
                    item.speed += 1

            if keyPress == 'k':  # Balls will move slower. Note that in our case min speed is 2.
                for item in BallList:
                    if item.speed > 2:
                        item.speed -= 1

            if keyPress == 's':  # Initial movement of balls
                for item in BallList:
                    if (not item.is_moving()):
                        if item.x_direction == 1:  # it means ball moves to right in x direction
                            item.xMovement = 1
                        else:  # it means ball moves to left in x direction
                            item.xMovement = -1
                        item.yMovement = -1  # at initial ball moves up in y direction


            gameTimer.value += 1
            for item in BallList:
                is_touch(item.x,item.y)
                gameOver = item.bounce(gameTimer.value, (myPaddle.x - int(myPaddle.width / 2)),
                          (myPaddle.x + int(myPaddle.width / 2)), win.getHeight() - margin - myPaddle.height)
                if len(BubblesList)==15:
                   for i in BallList:
                      i.shape.undraw()
                   #for a in ALLBubblesList:
                   #    if a not in BubblesList:
                   #        a.circle.undraw()
                   myPaddle.shape.undraw()
                   livesCounter.setText(f'Lives -- {lives}')
                   winmessage = Text(Point(150, 350), "GAME OVER\n\nYOU WIN!\n\nPress Any Key To Quit")
                   winmessage.setTextColor("Red")
                   winmessage.setSize(15)
                   winmessage.draw(win)
                   break
                if gameOver == True:
                    for i in BallList:
                        i.shape.undraw()
                        myPaddle.shape.undraw()
                    break
         lives-=1
         if lives==1 :
          livesCounter.setText(f'Lives -- {lives}')
         if lives==0:

             for i in BallList:
                 i.shape.undraw()
             print(len(ALLBubblesList))
             print(len(BubblesList))
             for a in ALLBubblesList:
                     a.circle.undraw()
             myPaddle.shape.undraw()
             #livesCounter.setText(f'Lives -- {lives}')
             winmessage = Text(Point(150, 350), "GAME OVER\n\nYOU LOST!\n\nPress Any Key To Quit")
             winmessage.setTextColor("Red")
             winmessage.setSize(15)
             winmessage.draw(win)

             break
         break
main()



