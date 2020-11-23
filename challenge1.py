# importing 
import math
import pyttsx3
en = pyttsx3.init()
en.setProperty("rate",125)

# Introduction
print('''Hello,My name is Jarvis.I am your personal assistant.
This is a simple program .This will help you to calculate
Use following shortcut:
Addition(1)
Subtraction(2)
Multiplication(3)
Division(4)
Square Root(5)
Square(6)''')
en.say("Hello,My name is Jarvis I am your personal assistant Use following shortcuts")
en.runAndWait()
# While loop
ch = 1
while ch == 1:
    a = int(input("Which program you want to use : "))
    en.runAndWait()
# Addition 
    if a == 1:
        print("Addition")
        b = int(input("First number : "))
        c = int(input("Second number : "))
        print("The addition of "+str(b)+" and "+str(c)+" is "+str(b+c))
# Subtraction 
    if a == 2:
        print("Subtraction")
        d = int(input("First number : "))
        e = int(input("Second number : "))
        print("The Subtraction of "+str(d)+" and "+str(e)+" is "+str(d-e))
# Multiplication 
    if a == 3:
        print("Multiplication")
        f = int(input("First number : "))
        g = int(input("Second number : "))
        print("The Multiplication of "+str(f)+" and "+str(g)+" is "+str(f*g))
# Division 
    if a == 4:
        print("Division")
        h = int(input("First number : "))
        i = int(input("Second number : "))
        print("The Division of "+str(h)+" and "+str(i)+" is "+str(h/i))
# Square root 
    if a == 5:
        print("Square root")
        j = int(input("Number : "))
        print("The Square root of "+str(j)+" is "+str(math.sqrt(j)))
# Square 
    if a == 6:
        print("Square")
        k = int(input("Number : "))
        print("The Square of "+str(k)+" is "+str(k**2))
    en.say("Thanks for using this program  Do you want to use it again")
    en.runAndWait()
    ch = int(input("Thanks for using this program . Do you want to use it again?(Yes(1),No(0)) : "))