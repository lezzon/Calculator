def menu():
    print ("Welcome to calculator")
    print ("Your options are:")
    print (" ")
    print ("1) Addition")
    print ("2) Subtraction")
    print ("3) Powering")
    print ("4) Quit calculator.py")
    print (" ")
    return int(input ("Choose your option: "))       
def add(a,b):
    return a + b
def sub(a,b):
    return b - a
def power(a,b):
    return a**b    
# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN   
loop = 1
choice = int()        # choice = 0 - the same action   
while (loop == 1):
    choice = menu() 
    if choice == 1: 
        a = int(input("Add this: "))
        b = int(input("to this: "))
        print (a, "+", b, "=", add(a,b))
    elif choice == 2:
        a = int(input("Subtract this: "))
        b = int(input("from this: "))
        print (b, "-", a, "=", sub(a,b))
    elif choice == 3:
        a = int(input("Take this: "))
        b = int(input("And power it by this: ")) 
        print(a,  "in the power of ", b, " =", power(a,b))   
    elif choice == 4:
        loop = 10  
print ("Thank you for using the calculator, you are a great user!")    