#************************************************************************************
#Getting started with python
print("Hello, world")
print("Please note this repo covers Intro to python")
print("Prepared by: Daniel Mwendwa")
#************************************************************************************

#Numeric Data types
print("Python has three numeric types: int, float, and complex")
myValue=1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue=3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue=5J
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
#************************************************************************************
#string Data types
myString="This is my string"
print(myString)
print(type(myString))
print(myString + " is of the data type "+ str(type(myString)))
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
#user input
name = input("What is your name? ")
print(name)
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))
#************************************************************************************

#Lists, Tuples, and Dictionaries
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
myFruitList[2] = "orange"
print(myFruitList)

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
#Conditional
age=19
if age>18:
    print("You are eligble to vote")
elif age==18:
    print("Apply for the National ID")
else:
    print("You cannot vote")
#************************************************************************************