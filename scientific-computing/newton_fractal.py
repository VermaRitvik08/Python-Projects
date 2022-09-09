import numpy as np
import matplotlib.pyplot as plt

pwr = input("Newton fractal z**n=1, Enter n (default 3): ")
if pwr == "":
    n = 3           #default setting for power of z
else:
    n = int(pwr)        #else the number given


sol=[]
for i in range(0,n):
    root = np.exp(2*np.pi*1j*i/n)   #formula for the roots of unity
    print(root)
    sol+=[root]     #store the solutions in a list

values = input("Enter xmin,xmax,ymin,ymax (default -1.35,1.35,-1.35,1.35):")
if values == "":
    xmin = -1.35        #default values 
    xmax = 1.35
    ymin = -1.35
    ymax = 1.35
else:
    xmin,xmax,ymin,ymax = values.split()
    xmin = float(xmin+0.00011)              #self set values
    xmax = float(xmax)
    ymin = float(ymin+0.00011)
    ymax = float(ymax)


x = np.linspace(xmin,xmax,1000)     #array of 1000 values for x and y
y = np.linspace(ymin,ymax,1000)

C=np.zeros((1000,1000),dtype=complex)   #start matrix size of 1000x1000

for i in range(1000):
    for j in range(1000):
        C[i,j]=x[j]+1j*y[999-i]     #formula for each entry of j and i in range 1000

for i in range(20):             #perform newton iterations for 20 times
    C = C - (C**n-1)/(n*C**(n-1))

row,column = C.shape    

color = np.zeros((row,column),dtype=int)
num1 = [0]*n    #empty list of size of power 
for i in range(row):
    for j in range(column):
        for m in range(n):
            num1[m] = abs(C[i,j]-sol[m])/abs(sol[m])    # the relative difference between a given element at position [i,j] in the C matrix
            color[i,j] = num1.index(min(num1))*255/(n-1)    #assign color for i and j


plt.imshow(color, cmap='rainbow', origin='lower', extent=(xmin,xmax,ymin,ymax),interpolation='bilinear')
plt.show()
#it takes a while for the fractal graph image to load