
import numpy as np

n1= float(input("Square root of which number? "))        #ask for number as input

def root(num):
    assume = num    #assumed number is same as input
    count =0        #counter to check if number reached root
    while True:
        count+=1
        root = 0.5*(assume + (num/assume))  #formula for newton raphson method
        print(count,root)       
        e = abs(root-assume)        #error to check how close it is 
        if (e<0.00001):         #if error is less than this value the loop ends
            break
        assume = root           #when at the end input is the same as the root value
    return ""

print(root(n1))                 #printing the function 

