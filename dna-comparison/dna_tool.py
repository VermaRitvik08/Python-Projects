#Import modules
from Patient import Patient
import random

#initialize global variable
random.seed(5) # random seed used for reproducibility
LENGTH_DNA=20


########################
##### Functions ########
########################

def display_menu():
    """ Display all the options, no input, no output """
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Compare all; 7-Analyze")
    


def random_base():
    """select the letter A,C,G,T at random, output (String) """
    bases=["A","C","G","T"]
    return random.choice(bases)

def random_strand():
    val = random_base() #initialize varibale which will produce random dna strand
    for i in range (0,19):  # length of patients in the list
        val += random_base()
    return val
    
    
def initialize(): #hardcoded all the patients which will be in initial list

    name = "Andrea"
    age = "37"
    dna = random_strand()
    p1 = Patient(name, age, dna)

    name = "Bob  "
    age = "28"
    dna = random_strand()
    p2 = Patient(name, age, dna)

    name = "Brooke"
    age = "34"
    dna = random_strand()
    p3 = Patient(name, age, dna)

    name = "Connor"
    age = "27"
    dna = random_strand()
    p4 = Patient(name, age, dna)

    name = "James"
    age = "25"
    dna = random_strand()
    p5 = Patient(name, age, dna)

    name = "Jenna"
    age = "44"
    dna = random_strand()
    p6 = Patient(name, age, dna)

    name = "John "
    age = "45"
    dna = random_strand()
    p7 = Patient(name, age, dna) 

    name = "Julie"
    age = "37"
    dna = random_strand()
    p8 = Patient(name, age, dna)

    name = "Kate "
    age = "48"
    dna = random_strand()
    p9 = Patient(name, age, dna)

    name = "Keith"
    age = "28"
    dna = random_strand()
    p10 = Patient(name, age, dna)

    name = "Kelly"
    age = "25"
    dna = random_strand()
    p11 = Patient(name, age, dna)

    name = "Luke "
    age = "33"
    dna = random_strand()
    p12 = Patient(name, age, dna)

    name = "Mark "
    age = "34"
    dna = random_strand()
    p13 = Patient(name, age, dna)

    name = "Pat  "
    age = "26"
    dna = random_strand()
    p14 = Patient(name, age, dna)

    name = "Taylor"
    age = "30"
    dna = random_strand()
    p15 = Patient(name, age, dna)

    name = "Tony "
    age = "55"
    dna = random_strand()
    p16 = Patient(name, age, dna)

    p = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16] #combine all patients into one variable so they all will display when called
    return p
    
def display(lst):
    if lst[0].has_condition == None:   #if there isn't and extra condition print the patient lists normally
        print("        Name    age     DNA-strand")
        print("---------------------------------------------")
        count = 0
        for l in lst: #for each patient
            count = count + 1
            print(count, l.name,l.age,l.strand,sep="\t")
    else: #otherwise print with a separate column with the name of disease
        print("        Name    age     DNA-strand               %s"%(lst[0].condition_name))
        print("---------------------------------------------------------------")
        count = 0
        for l in lst:
            count = count + 1
            print(count, l.name,l.age,l.strand,l.has_condition,sep="\t")

def info(lst):

    i = len(lst)+1
    x1=0    #counters which will update when a patient is in a particular age range
    x2=0
    x3=0
    x4=0
    x5=0
    x6=0
    age = 0
    for l in lst: 
        age += int(l.age)   #adding all ages in the list of patients
        if int(l.age) <=20:  #increment 1 to counter if there is one patient in age range
            x1 = x1 + 1
        elif 20 < int(l.age) < 30:
            x2 = x2 + 1           
        elif 30 <= int(l.age) <= 40:
            x3 = x3 + 1
        elif 40 < int(l.age) <= 50:
            x4 = x4 + 1
        elif 50 < int(l.age) <= 60:
            x5 = x5 + 1
        elif int(l.age) > 60:
            x6 = x6 + 1
    
    total = age / int(len(lst))    #formula to calculate the average 

    print("#Patients",len(lst))
    print("<20: " + str((x1/len(lst))*100) + "%")
    print("20's: " + str((x2/len(lst))*100) + "%")
    print("30's: " + str((x3/len(lst))*100) + "%")
    print("40's: " + str((x4/len(lst))*100) + "%")
    print("50's: " + str((x5/len(lst))*100) + "%")
    print(">=60: " + str((x6/len(lst))*100) + "%")
    print("Age mean: " + str(total))
    
    counter = 0
    o = lst[0].condition_name
    if lst[0].has_condition != None: #if there is an extra condition then then this will be printed
        for i in range(len(lst)):
            a = lst[i].has_condition
            if a == True:    #for each True in has_condition column increment 1 to counter
                counter +=1 
        print(str(o) + ": " + str((counter / len(lst)) * 100) + "%") #print % of patients with the disease
    
def add_new_patient(patients):
    lst = [Patient()]
    patients=patients + lst     #adding new patient to the existing patient list
    patients[len(patients)-1].name = input("Enter Name: ")    #patient attributes are transferred to the end of the list
    patients[len(patients)-1].age = input("Enter Age: ")
    patients[len(patients)-1].strand = input("Enter DNA strand: ")

    while len(patients[len(patients)-1].strand) != 20:  #condition if the input strand of dna is not 20 letters
        print("Bad input! -length must be 20")
        patients[len(patients)-1].strand = input("Enter DNA strand: ") #ask to input again if strand isn't 20
    return patients
    
def compare(num1,num2): 
    
    lst = "" #lst is empty string to store common strand of dna
     
    for i in range(len(num1.strand)): #length is same for each strand but I chose the first dna since it does not matter which one i chose
        if num1.strand[i] == num2.strand[i]:  #search for the common letter through each list based on position
            lst = lst + num1.strand[i]   #increment the letter which is common in list
        else:
            lst = lst + 'x'   #if not increment 'x' to list
    return lst

def check_completness(strand1):
    count = 0   #empty counter
    for s in strand1:  
        if s != 'x':   #for each letter that is not 'x' increment 1 
            count += 1
    return (count/20)*100    #percentage similar based on dna length
   
    
def compare_all(lst):
    for i in range(len(lst)-1):    
        for j in range(i+1,len(lst)):
            patient1 = lst[i]  #the first patient
            patient2 = lst[j]  #the second patient to compare
            tmp = compare(patient1,patient2)   #comparing the strands for each of the two patients above using previous function 
            percent = check_completness(tmp)   #calculating the percentage of similarity 
            if percent > 33:       #only print the value if the percent variable has value greater than 33%
                print(str(patient1.name) + " vs " + str(patient2.name) + ' ' + str(percent) + "%")

def find_pattern(lst,strand1,disease_name):

    for i in range(len(lst)): 
        lst[i].condition_name = disease_name 
        tmp1 = lst[i].strand  #dna strand of all the patients
        tmp = False   #set initially to false
        for k in range(len(tmp1)-len(strand1)):
            if tmp1[k:k+len(strand1)] == strand1:   #if the characters in strand1 are equal in list tmp1, the temp variable becomes true
                tmp = True
                break
        lst[i].has_condition = tmp   #re-iterate over the has_condition and return the either true or false

    counter = 0 
    
    for i in range(len(lst)):
        a = lst[i].has_condition
        if a == True:    #search how many True are there in the new column and increment them to a counter
            counter +=1 
    print("Patients with the " + str(disease_name) + " condition: " + str((counter / len(lst)) * 100) + "%")

### to complete






##########################
########## Main Function #  to uncomment step by step fo testing
##########################
                
def main():
    ##################### TEST FOR OPTION 1
    print("\n****TEST the random_strand function****")
    print(random_strand())

    ##################### TEST FOR OPTION 1
    print("\n****TEST the class Patient****")
    patient=Patient("Tom",20,random_strand())
    print(patient.name,patient.age,patient.strand)
    
    ##################### TEST FOR OPTION 1
    print("\n****TEST the display function****")
    patients=[patient,Patient()]
    patients[1].name="Lucy"
    patients[1].age=25
    patients[1].strand="TCTTGTAAACTCGGAAACTG"
    display(patients)

    ##################### TEST FOR OPTION 2
    #print("\n****TEST the info function****")
    #info(patients)
    

    ###################### TEST for OPTION 4
    #print("\n****TEST the add_new_patient function****")
    patients=add_new_patient(patients)
    display(patients)
    #info(patients)
    #find_pattern(patients,"CAT")
    ###################### TEST for OPTION 5
    #print("\n****TEST the compare function****")
    #common_strand=compare(patients[0],patients[1])
    #print(common_strand)

    ###################### TEST for OPTION 5
    #print("\n****TEST the check_completness function****")
    #print(check_completness(common_strand))
    #compare_all(patients)
    
if __name__=="__main__":
    main()