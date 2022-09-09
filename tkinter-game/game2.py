from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time
import random
#the racket and ball class are same as before files
class Racket:
    
    def __init__(self, mapping, canvas, lx=0, ly=0):
        self.mapping = mapping
        self.canvas = canvas 
        self.lx = lx
        self.ly = ly
        self.x = 0
        self.x1 = 0     #new initial point for the second racket 
        self.y = mapping.get_ymin()+ly/2
        self.y1 = mapping.get_ymax()-ly/2   #new initial point for second racket which is at the top
        self.racket = canvas.create_rectangle(mapping.get_i(self.x-lx/2),mapping.get_j(self.y+ly/2),mapping.get_i(self.x+lx/2+1),mapping.get_j(self.y-ly/2-1),fill="black")
        self.racket1 = canvas.create_rectangle(mapping.get_i(self.x-lx/2),mapping.get_j(self.y1-ly/2),mapping.get_i(self.x+lx/2+1),mapping.get_j(self.y1+ly/2-1),fill="black")
    
    
    """ to complete """

    def shift_left(self):
        if self.x - self.lx >= self.mapping.get_xmin():
            self.canvas.move(self.racket,-self.lx/2,0)
            self.x = self.x - self.lx/2

    def shift_right(self):
        if self.x + self.lx <= self.mapping.get_xmax():
            self.canvas.move(self.racket,self.lx/2,0)
            self.x = self.x + self.lx/2

    def shift_left1(self):                                  #I added 2 more methods which are the same as the ones before except this is for the second racket at the top
        if self.x1 - self.lx >= self.mapping.get_xmin():    # this racket updates x1 which is the points in x plane for the second racket
            self.canvas.move(self.racket1,-self.lx/2,0)
            self.x1 = self.x1 - self.lx/2

    def shift_right1(self):
        if self.x1 + self.lx <= self.mapping.get_xmax():
            self.canvas.move(self.racket1,self.lx/2,0)
            self.x1 = self.x1 + self.lx/2
    

class Ball:
    
    def __init__(self,mapping,canvas,x0,y0,velocity,angle,r):
        self.mapping = mapping
        self.canvas = canvas
        self.x0 = x0
        self.y0 = y0
        self.velocity = velocity
        self.angle = angle
        self.r = r
        
        self.x=0
        self.y=0
        self.ball = canvas.create_oval(mapping.get_i(self.x-self.r),mapping.get_j(self.y+self.r),mapping.get_i(self.x+self.r+1),mapping.get_j(self.y-self.r-1),fill="blue")
        

    def update_xy(self,t, offset=0,offset1=0): #second offset for the length of the second racket at the top
        

        x = self.x0 + self.velocity*t*math.cos(self.angle)
        y = self.y0 + self.velocity*t*math.sin(self.angle)
        
        ret = 0
        if x <= self.mapping.get_xmin()+self.r:  
             
            self.angle = (math.pi-self.angle)
            self.velocity=self.velocity
            self.x0 = x = self.mapping.get_xmin()+self.r
            self.y0 = y
              
            ret = 3
        elif self.mapping.get_xmax()-self.r <= x:
            self.angle = math.pi-self.angle
            self.velocity=self.velocity
            self.x0 = x = self.mapping.get_xmax()-self.r
            self.y0 = y
   
            ret = 4
                
        elif y <= self.mapping.get_ymin()+self.r+offset:
            self.angle = random.uniform(10,170)         #random angle 10 to 170 if ball bounces of racket
            self.velocity = self.velocity
              
            self.x0 = x
            self.y0 = y = self.mapping.get_ymin()+self.r+offset
               
            ret = 1
                
        elif y >= self.mapping.get_ymax()-self.r-offset1:   #this time there is offset at top so that ball can detect the racket 
            self.angle = random.uniform(-170,-10)       #random angle -10 to -170 if ball bounces of racket
            self.velocity = self.velocity
            
            self.x0 = x
            self.y0 = y = self.mapping.get_ymax()-self.r-offset1    #update y0
            
            ret = 2
        
        self.canvas.coords(self.ball, self.mapping.get_i(x-self.r),self.mapping.get_j(y-self.r),
                                        self.mapping.get_i(x+self.r),self.mapping.get_j(y+self.r))
        return ret



def main(): 
    
        m = Mapping_for_Tkinter(-600/2,600/2,-600/2,600/2,600)  #set mapping with size of canvas

        root = Tk() 
        canvas = Canvas(root,width=600,height=600)
        canvas.pack()
        root.update()
        
        ball1 = Ball(m,canvas,0,0,300,45*math.pi/180,600/120)   #initiate ball and racket with pre-set values for size of canvas, velocity and angle
        racket = Racket(m,canvas,600/10,600/60)
        
        canvas.bind("<Button-1>",lambda e:racket.shift_left1())     #start by controlling the top racket since the ball is travelling upwards
        canvas.bind("<Button-3>",lambda e:racket.shift_right1())
        canvas.itemconfig(racket.racket1,fill="red")
        t=0               # real time between event
        t_total=0         # real total time
        count=0           # rebound_total=0
        while True:
            t=t+0.01 #real time between events- in second
            t_total=t_total+0.01 #real total time- in second
            side=ball1.update_xy(t, 10, 10)# Update ball position and return collision event
            root.update()   # update the graphic (redraw)
            if side!=0:
                count=count+1 # increment the number of rebounds
                t=0 # reinitialize the local time
            time.sleep(0.01)  # wait 0.01 second (simulation time)
            
            if side==1: #if rebounds from bottom wall
                if ball1.x0 >= racket.x+racket.lx/2 or ball1.x0 < racket.x-racket.lx/2:
                    print("Game Over for racket 1!")
                    break
                else:   #same case as game1 except the if the ball does not hit the wall the other racket will gain control
                    canvas.itemconfig(racket.racket1,fill="red")       #when the ball rebounds from bottom racket the upper racket becomes red and lower stays black
                    canvas.itemconfig(racket.racket,fill="black")
                    canvas.bind("<Button-1>",lambda e:racket.shift_left1())
                    canvas.bind("<Button-3>",lambda e:racket.shift_right1())
            elif side==2:   #case for if ball rebounds from the top of the wall
                if ball1.x0 >= racket.x1+racket.lx/2 or ball1.x0 < racket.x1-racket.lx/2:
                    print("Game Over for racket 2!")
                    break
                else:   #same case and the other racket gains control if ball contacts racket
                    canvas.itemconfig(racket.racket,fill="red")     #when the ball rebounds from upper racket the lower racket turns red and the upper then becomes black
                    canvas.itemconfig(racket.racket1,fill="black")
                    canvas.bind("<Button-1>",lambda e:racket.shift_left())
                    canvas.bind("<Button-3>",lambda e:racket.shift_right())
        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()