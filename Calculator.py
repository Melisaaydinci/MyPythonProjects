from graphics import *

#Calculator

win=GraphWin('CALCULATOR',600,600)
rect1=Rectangle(Point(0,0),Point(600,100))  #sayının gireceği yer

rect2=Rectangle(Point(0,100),Point(150,200))    #ac ın gireceği yer
Text(rect2.getCenter(),'AC').draw(win)

rect3=Rectangle(Point(150,100),Point(300,200))  #+/- nin gireceği yer
Text(rect3.getCenter(),'+/-').draw(win)

rect4=Rectangle(Point(300,100),Point(450,200))  # % nın gireceği yer
Text(rect4.getCenter(),'%').draw(win)

rect5=Rectangle(Point(450,100),Point(600,200))  # / nın gireceği yer
Text(rect5.getCenter(),'/').draw(win)

rect6=Rectangle(Point(0,200),Point(150,300))    # 7 NİN YERİ
Text(rect6.getCenter(),'7').draw(win)

rect7=Rectangle(Point(150,200),Point(300,300))  # 8 İN YERİ
Text(rect7.getCenter(),'8').draw(win)

rect8=Rectangle(Point(300,200),Point(450,300))  # 9 un yeri
Text(rect8.getCenter(),'9').draw(win)

rect9=Rectangle(Point(450,200),Point(600,300))  # x nın yeri
Text(rect9.getCenter(),'x').draw(win)

rect10=Rectangle(Point(0,300),Point(150,400))   #4 ün yeri
Text(rect10.getCenter(),'4').draw(win)

rect11=Rectangle(Point(150,300),Point(300,400)) # 5 in yeri
Text(rect11.getCenter(),'5').draw(win)

rect12=Rectangle(Point(300,300),Point(450,400)) # 6 nın yeri
Text(rect12.getCenter(),'6').draw(win)

rect13=Rectangle(Point(450,300),Point(600,400)) # - nin yeri
Text(rect13.getCenter(),'-').draw(win)

rect14=Rectangle(Point(0,400),Point(150,500))   # 1 in yeri
Text(rect14.getCenter(),'1').draw(win)

rect15=Rectangle(Point(150,400),Point(300,500)) # 2 nin yeri
Text(rect15.getCenter(),'2').draw(win)

rect16=Rectangle(Point(300,400),Point(450,500)) # 3 ün yeri
Text(rect16.getCenter(),'3').draw(win)

rect17=Rectangle(Point(450,400),Point(600,500)) # + nın yeri
Text(rect17.getCenter(),'+').draw(win)

rect18=Rectangle(Point(0,500),Point(300,600))   #0 ın yeri
Text(rect18.getCenter(),'0').draw(win)

rect19=Rectangle(Point(300,500),Point(450,600)) #** ın yeri
Text(rect19.getCenter(),'**').draw(win)

rect20=Rectangle(Point(450,500),Point(600,600)) # = in yeri
Text(rect20.getCenter(),'=').draw(win)

myinput=Entry(Point(290,60),20)
write=Text(Point(290,10),'Calculator')
myinput.setText('0')
write.draw(win)
myinput.draw(win)
rect1.draw(win)
rect2.draw(win)
rect3.draw(win)
rect4.draw(win)
rect5.draw(win)
rect6.draw(win)
rect7.draw(win)
rect8.draw(win)
rect9.draw(win)
rect10.draw(win)
rect11.draw(win)
rect12.draw(win)
rect13.draw(win)
rect14.draw(win)
rect15.draw(win)
rect16.draw(win)
rect17.draw(win)
rect18.draw(win)
rect19.draw(win)
rect20.draw(win)


def main():
 myinputs=None
 mynewinputs = None
 islem = None
 try:
  while True:
   apoints=win.getMouse()
   xcordinate=apoints.getX()
   ycordinate=apoints.getY()

   if 0<=xcordinate<600 and 0<=ycordinate <100 : #en üstteki dikdörtgen
         pass
   if 0<=xcordinate<300 and 500<=ycordinate<600:  #0 ın olduğu yer
      if myinputs==None:
         myinputs='0'
      else:
         myinputs+='0'
      myinput.setText(myinputs)

   if 0<=xcordinate<150 and 200<=ycordinate<300:  #7
      if myinputs==None:
         myinputs='7'
      else:
         myinputs+='7'
      myinput.setText(myinputs)

   if 0<=xcordinate<150 and 300<=ycordinate<400: #4
      if myinputs==None:
         myinputs='4'
      else:
         myinputs += '4'
      myinput.setText(myinputs)

   if 0<=xcordinate<150 and 400<=ycordinate<500: #1
      if myinputs==None:
         myinputs='1'
      else:
         myinputs += '1'
      myinput.setText(myinputs)

   if 0<=xcordinate<150 and 100<=ycordinate<200:   #AC İÇİN
         myinputs=None
         mynewinputs=None
         myinput.setText('0')

   if 150<=xcordinate<300 and 200<=ycordinate<300: #8
      if myinputs==None:
         myinputs='8'
      else:
         myinputs += '8'
      myinput.setText(myinputs)

   if 150<=xcordinate<300 and 300<=ycordinate<400: #5
      if myinputs == None:
         myinputs = '5'
      else:
         myinputs += '5'
      myinput.setText(myinputs)

   if 150<=xcordinate<300 and 400<=ycordinate<500: #2
      if myinputs == None:
         myinputs = '2'
      else:
         myinputs += '2'
      myinput.setText(myinputs)

   if 150<=xcordinate<300 and 100<=ycordinate<200: #+/-
       if myinputs!=None:
           try:
            myinputs=str(int(myinputs)*(-1))
            myinput.setText(myinputs)
           except ValueError:
               myinputs = str(float(myinputs) * (-1))
               myinput.setText(myinputs)
       else:
           try:
             mynewinputs = str(int(mynewinputs) * (-1))
             myinput.setText(mynewinputs)
           except ValueError:
               mynewinputs = str(float(mynewinputs) * (-1))
               myinput.setText(mynewinputs)

   if 300<=xcordinate<450 and 200<=ycordinate<300:#9
      if myinputs == None:
         myinputs = '9'
      else:
         myinputs += '9'
      myinput.setText(myinputs)

   if 300<=xcordinate<450 and 300<=ycordinate < 400: #6
      if myinputs == None:
         myinputs = '6'
      else:
         myinputs += '6'
      myinput.setText(myinputs)

   if 300<=xcordinate<450 and 400<=ycordinate < 500: #3
      if myinputs == None:
         myinputs = '3'
      else:
         myinputs += '3'
      myinput.setText(myinputs)

   if 300<=xcordinate<450 and 100<=ycordinate<200:  #%
      if myinputs==None and islem==None:
           myinput.setText('0')
      elif myinputs==None and islem!=None:
          if islem == '=':
              myinput.setText(mynewinputs)
          else:
              mynewinputs=None
              myinput.setText('0')
      else:
        if mynewinputs == None:
         mynewinputs=myinputs
        elif islem=='+':
          try:
            mynewinputs=str(int(mynewinputs)+int(myinputs))
            myinput.setText(mynewinputs)
          except ValueError:
              mynewinputs = str(float(mynewinputs) + int(myinputs))
              myinput.setText(mynewinputs)
        elif islem=='-':
         try:
            mynewinputs=str(int(mynewinputs)-int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) - int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='x':
         try:
            mynewinputs=str(int(mynewinputs)*int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) * int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='/':
         try:
            mynewinputs=str(int(mynewinputs)/int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) / int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='%':
         try:
            mynewinputs=str(int(mynewinputs)%int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) % int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='**':
         try:
            mynewinputs=str(int(mynewinputs)**int(myinputs))
            myinput.setText(mynewinputs)
         except:
             mynewinputs = str(float(mynewinputs) ** int(myinputs))
             myinput.setText(mynewinputs)
        myinputs=None
      islem = '%'


   if 300<=xcordinate<450 and 500<=ycordinate<600:   # **
      if myinputs == None and islem==None:
          myinput.setText('0')
      elif myinputs==None and islem!=None:
          if islem == '=':
              myinput.setText(mynewinputs)
          else:
              mynewinputs=None
              myinput.setText('0')
      else:
        if mynewinputs == None:
          mynewinputs=myinputs
        elif islem == '+':
         try:
           mynewinputs = str(int(mynewinputs) + int(myinputs))
           myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) + int(myinputs))
             myinput.setText(mynewinputs)
        elif islem == '-':
         try:
           mynewinputs = str(int(mynewinputs) - int(myinputs))
           myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) - int(myinputs))
             myinput.setText(mynewinputs)
        elif islem == 'x':
         try:
           mynewinputs = str(int(mynewinputs) * int(myinputs))
           myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) * int(myinputs))
             myinput.setText(mynewinputs)
        elif islem == '/':
         try:
           mynewinputs = str(int(mynewinputs) / int(myinputs))
           myinput.setText(mynewinputs)
         except:
             mynewinputs = str(float(mynewinputs) / int(myinputs))
             myinput.setText(mynewinputs)
        elif islem == '%':
         try:
           mynewinputs = str(int(mynewinputs) % int(myinputs))
           myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) % int(myinputs))
             myinput.setText(mynewinputs)
        elif islem == '**':
         try:
           mynewinputs = str(int(mynewinputs) ** int(myinputs))
           myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) **int(myinputs))
             myinput.setText(mynewinputs)
        myinputs = None
      islem = '**'


   if 450<=xcordinate<600 and 100<=ycordinate < 200: #/
      if myinputs == None and islem==None:
          myinput.setText('0')
      elif myinputs==None and islem!=None:
          if islem == '=':
              myinput.setText(mynewinputs)
          else:
              mynewinputs=None
              myinput.setText('0')
      else:
        if mynewinputs == None:
          mynewinputs=myinputs
        elif islem=='+':
         try:
            mynewinputs=str(int(mynewinputs)+int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) + int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='-':
         try:
            mynewinputs=str(int(mynewinputs)-int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) - int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='x':
         try:
            mynewinputs=str(int(mynewinputs)*int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) * int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='/':
         try:
            mynewinputs=str(int(mynewinputs)/int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) / int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='%':
         try:
            mynewinputs=str(int(mynewinputs)%int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) % int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='**':
         try:
            mynewinputs=str(int(mynewinputs)**int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) ** int(myinputs))
             myinput.setText(mynewinputs)
        myinputs = None
      islem = '/'


   if 450<=xcordinate<600 and 200<= ycordinate < 300: #x
      if myinputs == None and islem==None:
         myinput.setText('0')
      elif myinputs==None and islem!=None:
          if islem=='=':
              myinput.setText(mynewinputs)
          else:
              mynewinputs=None
              myinput.setText('0')
      else:
        if mynewinputs == None:
         mynewinputs=myinputs
        elif islem=='+':
         try:
            mynewinputs=str(int(mynewinputs)+int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) + int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='-':
         try:
            mynewinputs=str(int(mynewinputs)-int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) - int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='x':
         try:
            mynewinputs=str(int(mynewinputs)*int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) * int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='/':
         try:
            mynewinputs=str(int(mynewinputs)/int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) / int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='%':
         try:
            mynewinputs=str(int(mynewinputs)%int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) % int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='**':
         try:
            mynewinputs=str(int(mynewinputs)**int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) ** int(myinputs))
             myinput.setText(mynewinputs)
        myinputs = None
      islem = 'x'


   if 450<=xcordinate<600 and 300<=ycordinate < 400: #-
      if myinputs == None and islem==None:
           myinput.setText('0')
      elif myinputs==None and islem!=None:
          if islem == '=':
              myinput.setText(mynewinputs)
          else:
              mynewinputs=None
              myinput.setText('0')
      else:
        if mynewinputs == None:
         mynewinputs=myinputs
        elif islem == '+':
         try:
           mynewinputs = str(int(mynewinputs) + int(myinputs))
           myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) + int(myinputs))
             myinput.setText(mynewinputs)
        elif islem == '-':
         try:
           mynewinputs = str(int(mynewinputs) - int(myinputs))
           myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) - int(myinputs))
             myinput.setText(mynewinputs)
        elif islem == 'x':
         try:
           mynewinputs = str(int(mynewinputs) * int(myinputs))
           myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) * int(myinputs))
             myinput.setText(mynewinputs)
        elif islem == '/':
         try:
           mynewinputs = str(int(mynewinputs) / int(myinputs))
           myinput.setText(mynewinputs)
         except:
             mynewinputs = str(float(mynewinputs) / int(myinputs))
             myinput.setText(mynewinputs)
        elif islem == '%':
         try:
           mynewinputs = str(int(mynewinputs) % int(myinputs))
           myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) % int(myinputs))
             myinput.setText(mynewinputs)
        elif islem == '**':
         try:
           mynewinputs = str(int(mynewinputs) ** int(myinputs))
           myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) ** int(myinputs))
             myinput.setText(mynewinputs)
        myinputs = None
      islem = '-'


   if 450<=xcordinate<600 and 400<=ycordinate < 500: #+
      if myinputs==None and islem==None:
       myinput.setText('0')
      elif myinputs==None and islem!=None:
          if islem == '=':
              myinput.setText(mynewinputs)
          else:
              mynewinputs=None
              myinput.setText('0')
      else:
        if mynewinputs==None:
         mynewinputs=myinputs
        elif islem=='+':
         try:
            mynewinputs=str(int(mynewinputs)+int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) + int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='-':
         try:
            mynewinputs=str(int(mynewinputs)-int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) - int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='x':
         try:
            mynewinputs=str(int(mynewinputs)*int(myinputs))
            myinput.setText(mynewinputs)
         except:
             mynewinputs = str(float(mynewinputs) * int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='/':
         try:
            mynewinputs=str(int(mynewinputs)/int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) / int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='%':
         try:
            mynewinputs=str(int(mynewinputs)%int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) % int(myinputs))
             myinput.setText(mynewinputs)
        elif islem=='**':
         try:
            mynewinputs=str(int(mynewinputs)**int(myinputs))
            myinput.setText(mynewinputs)
         except ValueError:
             mynewinputs = str(float(mynewinputs) ** int(myinputs))
             myinput.setText(mynewinputs)
        myinputs=None
      islem = '+'


   if 450 <= xcordinate < 600 and 500 <= ycordinate < 600:  # =
       if myinputs == None and islem==None:
           myinput.setText('0')
       elif myinputs == None and islem != None:
           mynewinputs = None
           myinput.setText('0')
       else:
           if mynewinputs == None:
               mynewinputs = myinputs
           elif islem == '+':
            try:
               mynewinputs = str(int(mynewinputs) + int(myinputs))
               myinput.setText(mynewinputs)
            except ValueError:
                mynewinputs = str(float(mynewinputs) + int(myinputs))
                myinput.setText(mynewinputs)
           elif islem == '-':
            try:
               mynewinputs = str(int(mynewinputs) - int(myinputs))
               myinput.setText(mynewinputs)
            except ValueError:
                mynewinputs = str(float(mynewinputs) - int(myinputs))
                myinput.setText(mynewinputs)
           elif islem == 'x':
            try:
               mynewinputs = str(int(mynewinputs) * int(myinputs))
               myinput.setText(mynewinputs)
            except ValueError:
                mynewinputs = str(float(mynewinputs) * int(myinputs))
                myinput.setText(mynewinputs)
           elif islem == '/':
            try:
               mynewinputs = str(int(mynewinputs) / int(myinputs))
               myinput.setText(mynewinputs)
            except ValueError:
                mynewinputs = str(float(mynewinputs) / int(myinputs))
                myinput.setText(mynewinputs)
           elif islem == '%':
            try:
               mynewinputs = str(int(mynewinputs) % int(myinputs))
               myinput.setText(mynewinputs)
            except ValueError:
                mynewinputs = str(float(mynewinputs) % int(myinputs))
                myinput.setText(mynewinputs)
           elif islem == '**':
            try:
               mynewinputs = str(int(mynewinputs) ** int(myinputs))
               myinput.setText(mynewinputs)
            except ValueError:
                mynewinputs = str(float(mynewinputs) ** int(myinputs))
                myinput.setText(mynewinputs)
           myinputs = None
       islem='='

 except GraphicsError:
    win.close()
main()
