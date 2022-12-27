def acronym(string):                          # Defining a function named as acronym
    
    string=string.lower()   
    w=string.split(' ')  
    
    acronym=''        
    
    ex=['of','an','a','the','and','&']        # List of strings or characters which shouldn't be in the phrase
    
    for i in w:
        if i not in ex: 
            acronym+=i[0].upper()
    print('acronym:',acronym)                 # Printing our result
choice=input("Enter any key to continue and 'stop' to terminate")  #choice for either starting or terminating

while choice!="stop":
    phrase=input("Enter the phrase")
    acronym(phrase)                           #calling the function
    choice=input("Enter any key to continue and 'stop' to terminate")
else:
    print("Thanks for trying the program!")
    
