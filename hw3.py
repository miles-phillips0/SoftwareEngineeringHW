import math
import os


#question 1
def VowelsVsConsonants(str):
    str = str.lower()
    vowles = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxyz"
    balance = 0
    for letter in str:
        if letter in vowles:
            balance += 1
        if letter in consonants:
            balance -=1
    
    if balance > 0:
        return True
    
    if balance < 0:
        return False
    
    return None

#question 2
def CylinderVolume(radius, height):
    return (2 * radius * height * math.pi)

#question 3
def CommaConcat(strList):
    combined = ""
    for str in strList:
        combined += (str + ", ")
    
    #this part just takes off the last comma
    combined = combined[0:len(combined)-2]
    return combined

#question 4
def ConcatFile(strLists):
    combined = ""
    f = open('output.txt' , 'w')
    for list in  strLists:
        combined += (CommaConcat(list) + ", ")
    
    combined = combined[0:len(combined)-2]
    f.write(combined)
    f.close()
    return os.path.abspath('output.txt')

#question 5
def FileToList(filePath):
    combined = []
    currentLine = []
    f = open(filePath , 'r')
    for line in f.readlines():  
        currentLine = line.split(", ")
        combined.append(currentLine)
    
    return combined

#question 6
def divideTwo(numerator, denominator):
    while True:
        try:
            divided = numerator / denominator
            return divided
        except ZeroDivisionError:
            print("divide by 0 error")
            denominator = int(input("Enter a new denominator: "))

#question 7
def noDuplicates(intList):
    newList = []
    for i in intList:
        if i not in newList:
            newList.append(i)
    return newList

#question 8
def createDirectory():
    path = os.getcwd() + "/hw3-folder"
    os.mkdir(path)

createDirectory()

