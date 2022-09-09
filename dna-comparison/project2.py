'''------------------------------------------------------
                 Import Modules 
---------------------------------------------------------'''
import dna_tool as dna

'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''


print("==============================================")
print('DNA "Analyzer" and Patient Management Tool')
print("==============================================")



test = dna.initialize()

while True:
    dna.display_menu()
    command=input("Command (Enter to exit): ")

    if command =="":
        print("\nThanks for using the DNA tool")
        print("Come back soon!")
        break      
        
    elif command == "1":
        dna.display(test) 

    elif command == "2":
        dna.info(test)   
    
    elif command == "3":
        index=int(input("Which patient would you like to remove? "))
        if not(1<=index<=len(test)):
            continue
        del(test[index-1])

    elif command == "4":
        test = dna.add_new_patient(test)
        
    
    elif command == "5":
        index1=int(input("First Patient (enter number): "))
        index2=int(input("Second Patient (enter number): "))
        p = dna.compare(test[index1-1],test[index2-1])
        d = dna.check_completness(p)
        print("Patient %s and Patient %s common strand is %s"%(index1,index2,p))
        print("They are similar at " + str(d) + "%")

    elif command == "6":
        dna.compare_all(test)

    elif command == "7":
        condition = input("Which condition are you looking for: ")
        there = input("Enter Sequence: ")
        dna.find_pattern(test,there,condition)
        
       
        

    