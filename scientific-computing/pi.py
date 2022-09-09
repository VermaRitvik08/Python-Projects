##################################################
###### IF YOU WORK BY GROUP OF TWO ###############
###### ENTER YOUR TWO NAMES HERE:  ###############
###### Name1=Ritvik Verma (only)
###### Name2=
######
###### Only 1 submission on moodle (either names ok)
##################################################
from numpy import random
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
N=1000000   #evaluate for 1 million values
x=np.random.uniform(-1,1,N)   #random values for x and y within N
y=np.random.uniform(-1,1,N)
estimate=np.zeros(x.shape)

n=0
inside=0
for i in range(len(x)):     #for values in million range
    if x[i]**2+y[i]**2<=1:    #check if random values are within the area of circle and add 1 to counter if so
        inside+=1
    estimate[i]=4*inside/(i+1)    #the formula for calculating pi
    
    if (i+1)==10**(n+1):      #if the number of evaluation is at a power of 10 within range, then print the Pi estimate and do so for all such 10 powers
        print('Using %s samples, pi is %s'%(i+1,estimate[i]))
        n=n+1

plt.figure(0)
plt.semilogx(estimate)  #convert x to log format
plt.xlabel('#samples')
plt.ylabel('pi')
plt.show()

theta = np.arange(0,2*np.pi,1/360)    #making a circle 
r1=1
x1 = np.array([])
y1 = np.array([])

for i in range(len(theta)):
    x1 = np.append(x1,r1*np.cos(theta[i])) 
    y1 = np.append(y1,r1*np.sin(theta[i])) 

n = [10, 100, 1000, 10000]  #the values for which the circle diagrams must form

plt.figure(1)
c = 1
for i in n:   #loop so that i can print all 4 circles instantly

    pi = estimate[i-1]  #the value of pi at numbers in n list
    plt.subplot(220+c)   #subplot to place the circle in corners 
    c+=1
    plt.plot(x[:i],y[:i],'r.')    #plotting the random dots for x and y until the i value reaches in list
    plt.plot(x1,y1,'b-')            #plotting the circle
    plt.axis('equal')
    plt.title("n=%i, pi= %.3f"%(i,pi))    #writing the value of pi at that iteration to 3 decimal places
    plt.xticks([])  #removing labels
    plt.yticks([])

plt.show()    #completing plot