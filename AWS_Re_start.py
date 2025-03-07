#************************************************************************************
#Getting started with python
import sys
print("Hello, world")
print("Please note this repo covers Intro to python")
print("Author: Daniel Mwendwa")
def next_session():
    response = input("Would you like to go to the next session? (yes/no): ").strip().lower()
    if response == "yes":
        print("Proceeding to the next session...")
    else:
        print("Exiting...")
        sys.exit()

next_session()
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
next_session()
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
next_session()
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
next_session()
#************************************************************************************
#Creating Mixed-type Lists
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
next_session()
#************************************************************************************
#Working with composite Data types
import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
myInventoryList = []
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("-----")
next_session()
#************************************************************************************
#Conditional
age=19
if age>18:
    print("You are eligble to vote")
elif age==18:
    print("Apply for the National ID")
else:
    print("You cannot vote")

userReply = input("Do you need to ship a cargo? (Enter Yes or No)")
if userReply=="Yes".strip().lower():
    print("We can Help you ship that package!")
else:
    print("Please come back when you need to ship a package")
    
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
next_session()
#************************************************************************************
#Working with Loops
#while loop
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random
number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

#for loop
print("Count to 10")
for x in range (1,11):
    print(x)
next_session()
#************************************************************************************
# Working with the String Sequence and Numeric Weight of Insulin in Python
# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = 	"rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin
# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human insulin, chain a: " + aInsulin)

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19 }  
# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))

molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
next_session()
#************************************************************************************
#using functions to implement caesar cipher
#This part covers Python functions
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
print(getDoubleAlphabet("ABC"))
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
runCaesarCipherProgram()
next_session()
#************************************************************************************
#creating File handlers and Modules  ---> Lab 126
import jsonFileHandler
data = jsonFileHandler.readJsonFile('insulin.json')
if data != "":
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    # Calculating the molecular weight of insulin  
    # Getting a list of the amino acid (AA) weights  
    aaWeights = data['weights']
    # Count the number of each amino acids  
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
    # Multiply the count by the weights  
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
    print("The rough molecular weight of insulin: " +
    str(molecularWeightInsulin))
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
else:
    print("Error. Exiting program")
next_session()
#************************************************************************************
#Python for system Admins --->Lab 128
import os
import subprocess

os.system("dir")  # Windows equivalent of 'ls'
subprocess.run(["cmd", "/c", "dir"])  # Run 'dir' in a subprocess
subprocess.run(["cmd", "/c", "dir", "/b", "README.md"])  # Equivalent to 'ls -l README.md'

command = "systeminfo"
print(f'Gathering system information with command: {command}')
subprocess.run(["cmd", "/c", command])

command = "tasklist"
print(f'Gathering active process information with command: {command}')
subprocess.run(["cmd", "/c", command])

#************************************************************************************
# using Debugger. This Lab explains how to use python debugger.
#debugger is a tools that is used to find bugs in a code. See instructions on how to use the python debugger online. Explore with this code.
name = "John"
print("Hello " + name + ".")
age = 40
print(name + " is " + str(age) + " years old.")
next_session()
#************************************************************************************
#Here is the addition of the for the python challenge code --> Lab 141
import os

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate prime numbers between 1 and 250
prime_numbers = [str(num) for num in range(1, 251) if is_prime(num)]

# Define file path and create directory if not exists
file_dir = "/home/user/prime_numbers"
os.makedirs(file_dir, exist_ok=True)
file_path = os.path.join(file_dir, "results.txt")

# Write results to a file
with open(file_path, "w") as file:
    file.write("\n".join(prime_numbers))

print(f"Prime numbers between 1 and 250 have been written to {file_path}")
#************************************************************************************
next_session()
print("CONGRATULATIONS!!!, You Have made it through the AWS python module")
print("I wish you all the best as you move to the Next session ---> Database")
print("Check out My Linkedin On the README File Just incase you need Clarification")
