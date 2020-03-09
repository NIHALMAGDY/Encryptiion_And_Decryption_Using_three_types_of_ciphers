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

alphabet = 'abcdefghigklmnopqrstuvwxyz'



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
                key = sys.argv[5]
                s2 = ""
                s3 = ""
                k = len(key)
                for i in range (0, len(Text)):
                    s3 += key[i%k]

                for i in range(0, len(Text)):
                    if Text[i].isalpha() and Text[i].isupper():
                       x  = chr(((ord(Text[i]) + ord(s3[i]) - 2 * ord('A')) % 26)+ord('A'))
                       s2+=x
                    elif s[i].isalpha() and s[i].islower():
                        x= chr(((ord(Text[i]) + ord(s3[i]) - 2 * ord('a')) % 26) + ord('a'))
                        s2+= x
                    else:
                        s2+=Text[i]
                OutputFile(s2)
                OutputFile.close()
    elif sys.argv[2] == "dec" :
    S = ""
    if sys.argv[2] == "enc" :
                key = sys.argv[5]
                s2 = ""
                s3 = ""
                k = len(key)
                for i in range (0, len(Text)):
                    s3 += key[i%k]

                for i in range(0, len(Text)):
                    if Text[i].isalpha() and Text[i].isupper():
                       x  = chr(((ord(Text[i]) - ord(s3[i]) - 2 * ord('A') + 78) % 26)+ord('A'))
                       s2+=x
                    elif s[i].isalpha() and s[i].islower():
                        x= chr(((ord(Text[i]) - ord(s3[i]) - 2 * ord('a') + 78) % 26) + ord('a'))
                        s2+= x
                    else:
                        s2+=Text[i]
                OutputFile(s2)
                OutputFile.close()
                
InputFile.close()

if __name__ == "__main__" :
    main()
