"""
UMass ECE 241 - Advanced Programming
Project #1   Fall 2021
project1.py - Sorting and Searching

"""


import matplotlib.pyplot as plt
import csv
import time
import random
from numpy import greater 


class BinarySearchTree:     #binary search tree from lecture notes

    def __init__(self, key=None, value=None):
        self.size = 0
        self.rightChild = None
        self.leftChild = None
        self.key = key
        self.value = value
        

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key=None, value=None):
        self.size += 1

        if self.key == None:
            self.key = key
            self.value = value
            return

        if self.key > key:
            if (self.leftChild == None):
                self.leftChild = BinarySearchTree()
            self.leftChild.put(key, value)
            return

        else:
            if (self.rightChild == None):
                self.rightChild = BinarySearchTree()
            self.rightChild.put(key, value)
            return

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def _get(self, key):
        if self.key < key and self.leftChild is not None:
            return self.leftChild.__getitem__(key)
        elif self.key > key and self.rightChild is not None:
            return self.rightChild.__getitem__(key)
        elif key == self.key:
            return self.value

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

"""
Stock class for stock objects
"""
class Stock:
    """
    Constructor to initialize the stock object
    """
    def __init__(self, sname, symbol, val, prices):
        self.sname = sname
        self.symbol = symbol
        self.val = val
        self.prices = prices
        #pass

    """
    return the stock information as a string, including name, symbol, 
    market value, and the price on the last day (2021-02-01). 
    For example, the string of the first stock should be returned as: 
    “name: Exxon Mobil Corporation; symbol: XOM; val: 384845.80; price:44.84”. 
    """
    def __str__(self):
        return "name: {}; symbol: {}; val: {}; price:{}".format(self.sname, self.symbol, self.val, self.prices[-1])
        
        #return the name, symbol, value and the latest price of the stocks


"""
StockLibrary class to mange stock objects
"""
class StockLibrary:

    """
    Constructor to initialize the StockLibrary
    """
    def __init__(self):     #instantiate everything given in the pdf
        self.stockList = []
        self.size = 0
        self.isSorted = False
        self.bst = None
        self.days = [4,5,6,7,8,11,12,13,14,15,19,20,21,22,25,26,27,28,29]   #to plot the dates along with the data
        #pass


    """
    The loadData method takes the file name of the input dataset,
    and stores the data of stocks into the library. 
    Make sure the order of the stocks is the same as the one in the input file. 
    """
   

    def loadData(self, filename: str):
        a = open(filename, 'r')
        b = a.readlines()
        
        for row in b[1:]:   #exclude first row since its a description
            stock = row.rstrip().split("|") #strip the '|' so that we can take each value individually
            self.stockList.append(Stock(stock[0], stock[1], float(stock[2]), stock[3:]))
            self.size+=1


    """
    The linearSearch method searches the stocks based on sname or symbol.
    It takes two arguments as the string for search and an attribute field 
    that we want to search (“name” or “symbol”). 
    It returns the details of the stock as described in __str__() function 
    or a “Stock not found” message when there is no match. 
    """
    def linearSearch(self, query: str, attribute: str):
        found = False   #at beginning we haven't found the name/symbol yet
        if attribute == "name":     
            for stock in self.stockList:    #search each stock in the stocklist
                if stock.sname == query:    #if we found the name, return true and show the stock found
                    found = True
                    return stock

        if attribute == "symbol":
            for stock in self.stockList:
                if stock.symbol == query:    #same process as the name, except here we are using symbols
                    found = True
                    return stock 
        if attribute != "symbol" or attribute != "name":    #if the attribute does not match any name or symbol, then it returns stock not found
            return ("Stock not found")

    """
    Sort the stockList using QuickSort algorithm based on the stock symbol.
    The sorted array should be stored in the same stockList.
    Remember to change the isSorted variable after sorted
    """
    def partition(self,low,high):           #partition, quicksortHelper, and quicksort code used from lecture notes
        pivotvalue = self.stockList[low]   
 
        leftmark = low+1
        rightmark = high

        done = False
        while not done:
 
            while leftmark <= rightmark and self.stockList[leftmark].symbol <= pivotvalue.symbol:   #since we are using quicksort for symbols, the comparison will also be between them 
                leftmark = leftmark + 1
 
            while self.stockList[rightmark].symbol >= pivotvalue.symbol and rightmark >= leftmark:
                rightmark = rightmark -1
 
            if rightmark < leftmark:
                done = True
            else:
                temp = self.stockList[leftmark]
                self.stockList[leftmark] = self.stockList[rightmark]
                self.stockList[rightmark] = temp
 
        temp = self.stockList[low]
        self.stockList[low] = self.stockList[rightmark]
        self.stockList[rightmark] = temp
 
 
        return rightmark
    
    def quickSortHelper(self,low,high):
        if low<high:
            splitpoint=self.partition(low,high)
            self.quickSortHelper(low, splitpoint - 1)
            self.quickSortHelper(splitpoint+1,high)

    """
    Sort the stockList using QuickSort algorithm based on the stock symbol.
    The sorted array should be stored in the same stockList.
    Remember to change the isSorted variable after sorted
    """
    def quickSort(self):
        self.quickSortHelper(0,len(self.stockList)-1)
        self.isSorted=True
 
    def graph(self):        
        f = self.stockList[0]
        for stock in self.stockList:    #code to compare the greatest length in the stockList
            if len(stock.sname) > len(f.sname):
                f = stock

        plt.plot(self.days,f.prices)    #days on x-axis and prices on y-axis
        plt.xlabel("Days")
        plt.ylabel("Prices of the stock")
        plt.title("Stock Price Data"+str(f.sname))
        plt.show()
        
        pass

    def change(self):
        difference1 = float(self.stockList[0].prices[-1])-float(self.stockList[0].prices[0])    #find the difference between the first and last value in the prices list
        difference2 = float(self.stockList[0].prices[-1])-float(self.stockList[0].prices[0])
        
        for stock in self.stockList:
            d = float(stock.prices[-1])-float(stock.prices[0])
            if d<difference2:   #search for greatest difference for loss
                difference2 = d     #set value if found greatest negative val
                loss = stock
            if d>difference1:   #search for greatest difference for profit
                difference1 = d     #set value if found greatest positive difference val
                profit = stock
        change1 = 100*(difference1/float(profit.prices[0])) #calculate percentages for profit and loss
        change2 = 100*(difference2/float(loss.prices[0]))
        print(profit)
        print(str(change1)+ ' % Profit')
        print(loss)
        print(str(change2)+' %'+' Loss')
        pass

    """
    build a balanced BST of the stocks based on the symbol. 
    Store the root of the BST as attribute bst, which is a TreeNode type.
    """
    def buildBST(self, l=None):
        if self.isSorted == False:
            self.quickSort()
        if l == None:
            l = self.stockList
        if len(l) < 1:
            return None
        if self.bst == None:
            self.bst = BinarySearchTree()
        
        mid = len(l)//2
        left_l = l[:mid]
        right_l = l[mid+1:]
        self.bst.put(l[mid].symbol, l[mid])
        self.buildBST(left_l)
        self.buildBST(right_l)
        

    """
    Search a stock based on the symbol attribute. 
    It returns the details of the stock as described in __str__() function 
    or a “Stock not found” message when there is no match. 
    """
    def searchBST(self, query, current='dnode'):
        current == 'dnode'
        pass
    
    def linearhundred(self):    #create function to find 100 random values from stockList
        randomval = []
        for i in range(100):
            randomval.append(self.stockList[i].symbol)  #find only functions 
        return randomval
        
    
    

# WRITE YOUR OWN TEST UNDER THIS IF YOU NEED
if __name__ == '__main__':

    stockLib = StockLibrary()
    testSymbol = 'GE'
    testName = 'General Electric Company'
    #testSymbol = 'MSFT'
    #testName = 'Microsoft Corporation'

    print("\n-------load dataset-------")
    stockLib.loadData("stock_database.csv")
    print(stockLib.size)

    
    print("\n-------linear search-------")
    
    print(stockLib.linearSearch(testSymbol, "symbol"))
    print(stockLib.linearSearch(testName, "name"))
   

    print("\n-------quick sort-------")
    
    print(stockLib.isSorted)
    stockLib.quickSort()
    print(stockLib.isSorted)
    
    print("\n------linear search time--------")
    t1 = time.time()
    for i in stockLib.linearhundred():
        stockLib.linearSearch(testSymbol, "symbol")
    t2 = time.time()
    tt = t2-t1
    print(str(tt)+" seconds")

    print("\n------bst time--------")
    t3 = time.time()
    for i in stockLib.linearhundred():
        stockLib.buildBST(stockLib.stockList)
    t4 = time.time()
    tt2 = t4-t3
    print(str(tt2)+" seconds")

    print("\n-------build BST-------")
    t5 = time.time()
    stockLib.buildBST()
    t6 = time.time()
    tt2 = t6-t5
    print(tt2)

    print("\n---------search BST---------")
    #print(stockLib.searchBST(testSymbol))
    

    stockLib.graph()
    stockLib.change()
