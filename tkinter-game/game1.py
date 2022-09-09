from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time
import random

#same racket class from before
class Racket:
    
    def __init__(self, mapping, canvas, lx=0, ly=0):
        self.mapping = mapping
        self.canvas = canvas 
        self.lx = lx
        self.ly = ly
        self.x = 0
        self.y = mapping.get_ymin()+ly/2
        self.racket = canvas.create_rectangle(mapping.get_i(self.x-lx/2),mapping.get_j(self.y+ly/2),mapping.get_i(self.x+lx/2+1),mapping.get_j(self.y-ly/2-1),fill="black")

    
    
    """ to complete """

    def shift_left(self):
        if self.x - self.lx >= self.mapping.get_xmin():
            self.canvas.move(self.racket,-self.lx/2,0)
            self.x = self.x - self.lx/2

    def shift_right(self):
        if self.x + self.lx <= self.mapping.get_xmax():
            self.canvas.move(self.racket,self.lx/2,0)
            self.x = self.x + self.lx/2
    

#same ball class as before
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
        
    #def coords(self):

    def update_xy(self,t, offset=0):    #added another argument offset which is the length of the racket
        

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
                
        elif y <= self.mapping.get_ymin()+self.r+offset:    #added an offset so that the ball can detect the racket and bounce off it as if it was a wall
            self.angle = -self.angle
            self.velocity = self.velocity
              
            self.x0 = x
            self.y0 = y = self.mapping.get_ymin()+self.r+offset #update y0 value
               
            ret = 1
                
        elif y >= self.mapping.get_ymax()-self.r:
            self.angle = random.uniform(-170,-10)   #using random angle when ever the ball hits the top of the canvas
            self.velocity = 1.25*self.velocity      #multiplying velocity by 1.25 times whenever it hits top wall
            
            self.x0 = x
            self.y0 = y = self.mapping.get_ymax()-self.r
            
            ret = 2
        
        self.canvas.coords(self.ball, self.mapping.get_i(x-self.r),self.mapping.get_j(y-self.r),
                                        self.mapping.get_i(x+self.r),self.mapping.get_j(y+self.r))
        return ret
        

def main(): 
    
        m = Mapping_for_Tkinter(-600/2,600/2,-600/2,600/2,600)

        root = Tk() 
        canvas = Canvas(root,width=600,height=600)
        canvas.pack()
        root.update()
        
        ball1 = Ball(m,canvas,0,0,200,30*math.pi/180,600/120)   #initiate both racket and ball in the canvas
        racket = Racket(m,canvas,600/10,600/60)

        canvas.bind("<Button-1>",lambda e:racket.shift_left())      #binding racket to mouse
        canvas.bind("<Button-3>",lambda e:racket.shift_right())
        
        ############################################
        ####### start simulation
        ############################################
        t=0               # real time between event
        t_total=0         # real total time
        count=0           # rebound_total=0
        while True:
            t=t+0.01 #real time between events- in second
            t_total=t_total+0.01 #real total time- in second
            side=ball1.update_xy(t, 10)# Update ball position and return collision event
            root.update()   # update the graphic (redraw)
            if side!=0:
                count=count+1 # increment the number of rebounds
                t=0 # reinitialize the local time
            time.sleep(0.01)  # wait 0.01 second (simulation time)
            if side==1:                                                                     #ret = 1 is case when the ball hits the bottom wall
                if ball1.x0 >= racket.x+racket.lx/2 or ball1.x0 < racket.x-racket.lx/2:     #if the ball hits the wall to the right of the racket or the left side of racket
                    break                                                                   #the simulation breaks
                
        print("Game over! Total time: %ss"%t_total)
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()