#Conditional Statements, Logical Operators, Code blocks and Scope
#roller coaster example
#print("Welcome to the roller coaster")
#height = int(input("What is your height in cm?"))

#if height <= 120:
    #print("You can ride the roller coaster")
#else:
    #print("You are not eligible to ride")
"""
number = int(input("which number do u want to check? "))

if number % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")

#nested if and else and elif statement


height = int(input("what is your height in cm? "))
age = int(input("what is your age"))
bill = 0

if height <= 120:
    print("You can ride the roller coaster")
    if age < 12:
       #print("pay $5")
       #assign each age payment amount to the bill
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
     #print("Please pay $7. ")
      bill = 7
      print("Youth tickets are $7")
    else:
      #print("Please pay $12")
       bill = 12
       print("Adult tickets are $12")
    
    wantsPhoto = input("Do you want a photo taken? Y OR N. ")
    if wantsPhoto == "Y":
    #Add $3 to their bill
       bill += 3
    print(f"Your final bill is {bill}")
else:
    print("You are not eligible to ride")
"""

'''
#BMI 2.0 Challenge
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))

bmi = weight / height ** 2
result = round(bmi)

if result < 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif  result < 25:
    print(f"Your BMI is {result}, you have a normal weight.")
elif  result < 30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif  result < 35:
    print(f"Your BMI is {result}, you are obese.")
else:
    print(f"Your BMI is {result}, you are clinically obese.")

#Leap Year Challenge
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
       if year % 400 == 0:
           print("Leap year")
       else:
           print("Not Leap year")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
'''
#Pizza order Exercise
print("Welcome to williams Pizza Deliveries! ")
size = input("What size pizza do you want? S, M, or L ")
addPepperoni = input("Do you want pepperoni? Y or N ")
extraCheese = input("Do you want extra cheese? Y or N ")

bill = 0
#Code for Small pizza
if size == 'S':
    bill+= 15
    if addPepperoni=='Y':
        bill+= 2
    elif addPepperoni=='N':
        pass
    if extraCheese== "Y":
        bill += 1
    elif extraCheese=="N":
        pass
    finalBill = round(bill)
    print(f"Your final bill is: ${finalBill}.")
else:
    #code for medium and large pizzas
    if size =='M':
        bill+=20
        if addPepperoni=='Y':
            bill+= 3
        elif addPepperoni=='N':
            pass
        if extraCheese=="Y":
            bill+= 1
        elif extraCheese=="N":
            pass
        finalBill=round(bill)
        print(f"Your final bill is: ${finalBill}.")
    else:
       if size =='L':
           bill+=25
           if addPepperoni=='Y':
               bill+= 3
           elif addPepperoni=='N':
               pass
           if extraCheese=="Y":
               bill+= 1
           elif extraCheese=="N":
               pass
           finalBill=round(bill)
           print(f"Your final bill is: ${finalBill}.")
           
               
    
