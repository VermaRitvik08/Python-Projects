import numpy as np
from numpy import random 
import matplotlib.pyplot as plt

np.random.seed(7)
N=100000

point1 = input("Enter (x,y) of point-1, default is (0.5,0.5): ")
if point1 == "":
    x1 = 0.5            #setting default values for all points of the triangle
    y1 = 0.5
else:
    x1,y1 = point1.split()          #self setting values for all points of the traingle
    x1 = float(x1)                  #float because the points can be in decimals too
    y1 = float(y1)

point2 = input("Enter (x,y) of point-2, default is (3,2.5): ")
if point2 == "":
    x2 = 3
    y2 = 2.5
else:
    x2,y2 = point2.split()
    x2 = float(x2)
    y2 = float(y2)

point3 = input("Enter (x,y) of point-3, default is (1,3): ")
if point3 == "":
    x3 = 1
    y3 = 3
else:
    x3,y3 = point3.split()
    x3 = float(x3)
    y3 = float(y3)


A = np.array([[x1, x2, x3], [y1, y2, y3],[1,1,1]])      #the matrix as shown in the pdf 
print("Barycentric Matrix",A,sep="\n")

x=np.random.uniform(min(x1,x2,x3),max(x1,x2,x3),N)      #setting the domain and range of the traingle diagram
y=np.random.uniform(min(y1,y2,y3),max(y1,y2,y3),N)



area = []

n=0
insideCount=0
for i in range(len(x)):
    var1 = np.array([x[i],y[i],1])      #the matrix as shown in pdf 
    solve = np.linalg.solve(A, var1)    #solving the matrix for values of a1 a2 and a3
    if solve[0]>= 0 and solve[1]>= 0 and solve[2] >= 0: #if the values of a1 a2 and a3 are greater than 0 then one dot increases in the triangle
      insideCount+=1
    area.append((max(x1,x2,x3)-min(x1,x2,x3))*(max(y1,y2,y3)-min(y1,y2,y3))*insideCount/(i+1))      #formula for the area of traingle according to pdf
    
    if (i+1)==10**(n+1):        #if iterations value reaches a power of 10 print the number of samples
        print('Using %s samples, pi is %s'%(i+1,area[i]))     #print the area
        n=n+1

plt.semilogx(area)
plt.show()


xt=[[x1],[x2],[x3],[x1]]    #making an array for the x and y values so that they form a triangle
yt=[[y1],[y2],[y3],[y1]]

n = [10, 100, 1000, 10000]      #values for which we need triangle diagram

plt.figure(1)
c = 1
for i in n:

    plt.subplot(220+c)
    c+=1
    plt.plot(x[:i],y[:i],'r.')  #plotting dots till value reaches i
    plt.plot(xt,yt,'b-')        #plotting the triangle
    
    plt.title("n=%i, pi= %.3f"%(i,area[i-1]))   
    plt.xticks([])      #remove labels
    plt.yticks([])

plt.show()      #plot all diagrams

