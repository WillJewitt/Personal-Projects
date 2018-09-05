#Calculator Program
import random
import tkinter

def add():      #Addition Function
    A1 = int(input('Input 1: '))        #Asks for the first input
    A2 = int(input('Input 2: '))        #Asks for the second input
    awnserA = str(A1 + A2)              #Creates a variable called AnswerA which contains A1 + A2

    print(str('The answer is ') + awnserA)

def multiply():     #Multiplication function
    M1 = int(input('Input 1: '))       #Asks for the first input
    M2 = int(input('Input 2: '))        #Asks for the second input
    awnserM = str(M1 * M2)              #Creates a variable called AnswerA which contains M1 x M2

    print(str('The answer is ') + awnserM)      #Prints the answer in a sentence

def divide():
    D1 = int(input('Input 1: '))
    D2 = int(input('Input 2: '))
    awnserD = str(D1 / D2)

    print(str('The awnser is ') + awnserD)

def square():
    S1 = int(input('Enter the number you want to be squared: '))
    answerS = str(S1 * S1)

    print(str('The answer is ' + answerS))

