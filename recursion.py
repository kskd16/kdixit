"""recursion  --functions which calls itself again and again is called recursion  eg: factorial,fibonacci series"""
"""local variable can be accessed within a function
global variable can be accessed throughout the code 
local can be changed to global by using 'global'"""
#recursion
#factorial of a number
def fact(no):
    if no==0 or no==1:
        return 1
    else:
        return (no*fact(no-1))
no=int(input("enter a no."))
print(fact(no))
