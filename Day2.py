#Datatype Challenge
#write a program that adds the digit in a 2 digits number
#two_digit_number = input("Type a two digit number: ")

#first_digit = two_digit_number[0]
#second_digit = two_digit_number[1]

#result = int(first_digit) + int(second_digit)
#print(result)

#mathematical operation
# +Addition -Subtraction /Division **Raise to the power //flow division(use to round up number)
#BMI Calculator
#height = input("enter your height: ")
#weight = input("enter your weight: ")

#bmi = int(weight) / float(height) ** 2
#print(int(bmi))

#value1 = int(input("Please enter a number: "))
#value2 = int(input("Please enter another number: "))
#sum = value1 + value2
#print(value1, "+", value2, "=", sum)
#Life in weeks exercise
#age = input("what is your current age? ")
#daysLeft = 90 - int(age)
#days = daysLeft * 365
#weeks = daysLeft * 52
#months = daysLeft * 12
#print(f"You have {days} days, {weeks} weeks, and {months} months left")

#Day2 Project(Tip Calculator)
print("Welcome to the tip calculator")
bill = input("What was the total bill? ")
billPercentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

splitBillPercentage = (int(billPercentage) / 100) * float(bill) + float(bill)
totalAmountPerPerson = (splitBillPercentage / int(people))
finalAmount = round(totalAmountPerPerson, 2)
print(f"Each person should pay {finalAmount}")

