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
def cylinderVolume(radius, height):
    return (2 * radius * height * math.pi)

#question 3
def commaConcat(strList):
    combined = ""
    for str in strList:
        combined += (str + ", ")
    #this part just takes off the last comma
    combined = combined[0:len(combined)-2]
    return combined

#question 4
def concatFile(strLists):
    combined = ""
    f = open('output.txt' , 'w')
    for list in  strLists:
        combined += (commaConcat(list) + ", ")
    combined = combined[0:len(combined)-2]
    f.write(combined)
    f.close()
    return os.path.abspath('output.txt')

listList = [["this", "is"], ["a"], ["test", "!"]]
concatFile(listList)

