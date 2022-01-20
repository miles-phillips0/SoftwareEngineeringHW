#question One
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

print(VowelsVsConsonants("faaaaeeeeiii"))


