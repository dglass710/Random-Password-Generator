from random import choice
from string import *
from sys import argv

def main(passLen = 16):
    'Returns a random string of length passLen which includes letters, digits, and special characters'
    password = ''
    for _ in range(passLen):
        password += choice(ascii_uppercase + ascii_lowercase + digits + punctuation)
    return password

def multiplePasswords(passLen, n):
    'Calls main passing passLen n times'
    passList = []
    for _ in range(n):
        passList.append(main(passLen))
    return passList

def multiplePasswordsCli(passLen):
    passList = []
    try:
        val = eval(argv[1])
    except:
        val = 20
    for _ in range(val):
        passList.append(main(passLen))
    return passList

# print(main(32))  # Generates and prints one single password of length 32

# for elem in multiplePasswords(25, 300): # Generates a list of 300 passwords each of length 25 and prints each element
#     print(elem)

# for elem in multiplePasswordsCli(16): # Generates a list of passwords the length of a number given as a command line option or 20 otherwise
#     print(elem)
