import sys
from string import ascii_uppercase, ascii_lowercase
from math import gcd
InputFile = open(sys.argv[3],"r")
Text = InputFile.read()
OutputFile = open(sys.argv[4],"w")

def generateKey(string, key):
    count = 0
    for char in string:
        if char.isalpha():
            count += 1

    key = list(key)
    if count == len(key):
        return (key)
    else:
        for i in range(count -
                       len(key)):
            key.append(key[i % len(key)])

    return ("".join(key))

def caesar_encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper() and char.isalpha():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower() and char.isalpha():
            result += chr((ord(char) + s - 97) % 26 + 97)
        elif char == ' ':
            result += ' '
        else:
            result += char

    return result

def caesar_decrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper() and char.isalpha():
            result += chr((ord(char) + 65 - s) % 26 + 65)
        elif char.islower() and char.isalpha():
            char = char.upper()
            char = chr((ord(char) + 65 - s) % 26 + 65)
            char = char.lower()
            result += char
        elif char == ' ':
            result += ' '
        else:
            result += char

    return result

def computeGCD(x, y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 


if sys.argv[1] == "shift" :
    S = ""
    if sys.argv[2] == "enc" :
        a = int(sys.argv[5])
        for ch in Text :
            x = ch
            if x != " " and x != "\n" :
                if (x.isupper()): 
                    x = chr((ord(x) + a - 65) % 26 + 65)
                elif (x.lower()):
                    x = chr((ord(x) + a - 97) % 26 + 97) 
                S+=x
        OutputFile.write(S)
        OutputFile.close()
    elif sys.argv[2] == "dec" :
        a = int(sys.argv[5])
        for ch in Text :
            x = ch
            if x != " " and x != "\n" :
                if (x.isupper()): 
                    x = chr((ord(x) + 65 - a) % 26 + 65)
                elif (x.islower()):
                    x = x.upper()
                    x = chr((ord(x) + 65 - a) % 26 + 65)
                    x = x.lower()
                S+=x
        OutputFile.write(x)
        OutputFile.close()

if sys.argv[1] == "affine" :
    S = ""
    if sys.argv[2] == "enc" :
            a = int(sys.argv[5])
            b = int(sys.argv[6])
            if gcd(a, 26) != 1:
                raise ValueError('a and 26 are not coprime. Please enter another key.')
            else:
                for ch in Text :
                    x = ch
                    if x != " " and x != "\n" :
                        if (x.isupper()): 
                            y = ((a * ascii_uppercase.index(ch)) + b) % 26
                            S += ascii_uppercase[y]
                        elif (x.islower()):
                            y = ((a * ascii_lowercase.index(ch)) + b) % 26
                            S += ascii_lowercase[y]
                        S+=x
                        
                OutputFile.write(S)
                OutputFile.close()
    elif sys.argv[2] == "dec" :
            S = ""
            counter = 1
            n = 1
            a = int(sys.argv[5])
            b = int(sys.argv[6])
            if gcd(a, 26) != 1:
                raise ValueError('a and 26 are not coprime. Please enter another key.')
            else :
                while True:
                    if a * n > 26 * counter:
                        if a * n == (26 * counter) + 1:
                            break
                        counter += 1
                    n += 1    
                for ch in Text :
                    x = ch
                    if x != " " and x != "\n" :
                        if (x.isupper()): 
                            d = int((n * (ascii_uppercase.index(ch) - b)) % 26)
                            S += ascii_uppercase[d]
                        elif (x.islower()):
                            d = int((n * (ascii_lowercase.index(ch) - b)) % 26)
                            S += ascii_lowercase[d]
                        S+=x
                OutputFile.write(S)
                OutputFile.close()
            
if sys.argv[1] == "vigenere" :
    S = ""
    if sys.argv[2] == "enc" :
                a = sys.argv[5]
                key = generateKey(Text, a)
                OutputFile(caesar_encrypt(Text, key))
                OutputFile.close()
    elif sys.argv[2] == "dec" :
                a = sys.argv[5]
                key = generateKey(Text, a)
                OutputFile(caesar_decrypt(Text, key))
                OutputFile.close()
                
InputFile.close()