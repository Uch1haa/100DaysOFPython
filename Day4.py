import random
"""
#generating random integers
randomInteger = random.randint(1, 10)
print(randomInteger)

#generating random floating point number
randomFloat = random.random()
print(randomFloat)

#Heads or Tails Exercise
headsTails = random.randint(0, 1)

if headsTails == 0:
    print("Tails")
else:
    print("Heads")
    
print(headsTails)

#Understanding the Offset and Appending Items to lIST
#List
#fruits = ["Orange", "Apple", "Strawberry", "Mango"]
#print(fruits)

#Banker Roulette Exercise
#Split string method
namesString = input("Give me everybody's names, separated by a coma. ")
names = namesString.split(", ")
listLength = len(names)
randomPick = random.randint(0, listLength -1)
personPaying = names[randomPick]

print(personPaying + " is going to buy the meal today")
"""
#Nested List
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][1])
#list = eval(input("Enter a list: "))
#print("The first element is ", list[0])
