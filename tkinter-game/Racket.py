from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *

class Racket:
    
    def __init__(self, mapping, canvas, lx=0, ly=0):
        self.mapping = mapping
        self.canvas = canvas 
        self.lx = lx
        self.ly = ly
        self.x = 0
        self.y = mapping.get_ymin()+ly/2
        self.racket = canvas.create_rectangle(mapping.get_i(self.x-lx/2),mapping.get_j(self.y+ly/2),mapping.get_i(self.x+lx/2+1),mapping.get_j(self.y-ly/2-1),fill="black")

        # self.x and self.y are the initial points of the racket
        #created a rectangle object which is our racket
    """ to complete """

    def shift_left(self):
        if self.x - self.lx >= self.mapping.get_xmin():  #the racket will only move if its width is less than the xmin value of the mapping
            self.canvas.move(self.racket,-self.lx/2,0)   #moving towards left
            self.x = self.x - self.lx/2

    def shift_right(self):
        if self.x + self.lx <= self.mapping.get_xmax(): #the racket will only move if its width is less than the xmax value of the mapping
            self.canvas.move(self.racket,self.lx/2,0)   #moving towards right
            self.x = self.x + self.lx/2
    

    

def main():

    ###### create a mapping
    swidth=input("Enter window size in pixels (press Enter for default 600): ")
    if swidth=="":
        width=600
    else:
        width=int(swidth)

    """ to complete """
    ##### create a window, canvas, and racket

    m = Mapping_for_Tkinter(-width/2,width/2,-width/2,width/2,width)        #set the mapping for the canvas

    root = Tk() 
    canvas = Canvas(root,width=width,height=width)
    canvas.pack()
    root.update()


    racket = Racket(m,canvas,width/10,width/60) #initiate racket in the canvas with lx as 1/10th of given width and ly 1/60th of given width

    canvas.bind("<Button-1>",lambda e:racket.shift_left())   #binding both sides to mouse
    canvas.bind("<Button-3>",lambda e:racket.shift_right())

    
    root.mainloop()
    """ to complete """
    
    



    

if __name__=="__main__":
    main()

