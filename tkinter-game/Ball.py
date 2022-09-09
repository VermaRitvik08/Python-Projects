from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time

class Ball:
    
    def __init__(self,mapping,canvas,x0,y0,velocity,angle,r):
        self.mapping = mapping
        self.canvas = canvas
        self.x0 = x0
        self.y0 = y0
        self.velocity = velocity
        self.angle = angle
        self.r = r
        
        self.x=0    #initial positions of x and y for the ball
        self.y=0
        self.ball = canvas.create_oval(mapping.get_i(self.x-self.r),mapping.get_j(self.y+self.r),mapping.get_i(self.x+self.r+1),mapping.get_j(self.y-self.r-1),fill="blue")
        
        #I included r as an instance argument since it depends on the given width otherwise it may look too small or big
        #created a circle object which will serve as our ball 
    def update_xy(self,t):
        

        x = self.x0 + self.velocity*t*math.cos(self.angle)  #x and y in terms of the time passed since ball started bouncing 
        y = self.y0 + self.velocity*t*math.sin(self.angle)
        
        ret = 0
        if x <= self.mapping.get_xmin()+self.r:  #if ball bouncing in the left wall
             
            self.angle = (math.pi-self.angle)
            self.velocity=self.velocity
            self.x0 = x = self.mapping.get_xmin()+self.r  #update x0 since the position now changed
            self.y0 = y
              
            ret = 3
        elif self.mapping.get_xmax()-self.r <= x:   #if ball bouncing in the right wall
            self.angle = math.pi-self.angle
            self.velocity=self.velocity
            self.x0 = x = self.mapping.get_xmax()-self.r #update x0 and y0
            self.y0 = y
   
            ret = 4
                
        elif y <= self.mapping.get_ymin()+self.r:   #if ball bounces at the bottom of canvas
            self.angle = -self.angle
            self.velocity = self.velocity
              
            self.x0 = x
            self.y0 = y = self.mapping.get_ymin()+self.r    #update x0 and y0
                
            ret = 1
                
        elif y >= self.mapping.get_ymax()-self.r:   #if ball bounces at the top of the canvas
            self.angle = -self.angle
            self.velocity = self.velocity
                
            self.x0 = x
            self.y0 = y = self.mapping.get_ymax()-self.r
            
            ret = 2
                
     
        self.canvas.coords(self.ball, self.mapping.get_i(x-self.r),self.mapping.get_j(y-self.r),
                                        self.mapping.get_i(x+self.r),self.mapping.get_j(y+self.r))
        #this updates all the coordinates of the ball in the mapping in terms of x and y axis
        return ret
        


def main(): 
        ##### create a mapping
        swidth=input("Enter window size in pixels (press Enter for default 600): ")
        if swidth=="":
            width=600
        else:
            width=int(swidth)

        #the same code to ask for size or use default
        """ to complete """
        
        ##### User Input 
        data=input("Enter velocity and theta (press Enter for default: 500 pixel/s and 30 degree):")
        
        if data=="":
            velocity=500
            angle=30
        else:
            velocity,angle = data.split()
            velocity = int(velocity)
            angle = int(angle)

        #asking for the velocity and angle from user, seet default values to 500 and 30

        """ to complete """

        """ to complete """
        m = Mapping_for_Tkinter(-width/2,width/2,-width/2,width/2,width)

        root = Tk() 
        canvas = Canvas(root,width=width,height=width)
        canvas.pack()
        root.update()
        
        ball1 = Ball(m,canvas,0,0,velocity,angle*math.pi/180,width/120)   #initiate ball based on the size of canvas, velocity and angle given by user or default
        
        ############################################
        ####### start simulation
        ############################################
        t=0               # real time between event
        t_total=0         # real total time
        count=0           # rebound_total=0
        while True:
            t=t+0.01 #real time between events- in second
            t_total=t_total+0.01 #real total time- in second
            side=ball1.update_xy(t)# Update ball position and return collision event
            root.update()   # update the graphic (redraw)
            if side!=0:
                count=count+1 # increment the number of rebounds
                t=0 # reinitialize the local time
            time.sleep(0.01)  # wait 0.01 second (simulation time)
            if count==10: break # stop the simulation
            
        print("Total time: %ss"%t_total)
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

