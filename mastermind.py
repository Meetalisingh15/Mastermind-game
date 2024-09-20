#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dines
#
# Created:     19-09-2024
# Copyright:   (c) dines 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
COLORS=["R","G","B","Y","W","O"]
TRIES=10
CODE_LENGTH=4
def generate_code():
    code=[]
    for i in range(CODE_LENGTH):
        color=random.choice(COLORS)
        code.append(color)
    return code
def guess_code():

    while True:
        guess=input("Guess: ").upper().split(" ")

        if len(guess)!=CODE_LENGTH:
            print(f"you must guess {CODE_LENGTH} colors.")
            continue
        for color in guess:
            if color not in COLORS:
                print(f"invalid color:{color}.Try again.")
                break
        else:
            break
    return guess
def check_code(guess,real_code):
    color_count={}
    correct_pos=0
    incorrect_pos=0
    for color in real_code:
        if color not in color_count:
            color_count[color]=0
        color_count[color]+=1
    for guess_color,real_color in zip(guess,real_code):
        if guess_color==real_color:
            correct_pos+=1
            color_count[guess_color]-=1
    for guess_color,real_color in zip(guess,real_code):
        if guess_color!=real_color and guess_color in color_count and color_count[guess_color]>0:
            incorrect_pos+=1
            color_count[guess_color]-=1
    return correct_pos,incorrect_pos
def game():
    print(f"welcome to mastermind,you have {TRIES} tries to guess the code...")
    print("the valid colors are:",COLORS)
    code=generate_code()
    for attempts in range(1,TRIES+1):
        guess=guess_code()
        correct_pos,incorrect_pos=check_code(guess,code)

        if correct_pos==CODE_LENGTH:
            print(f"you guessed  the code in {attempts} tries!")
            break
        print(f"correct positions:{correct_pos} | incorrect  positions:{incorrect_pos}")
    else:
        print("you ran out of tries,the code was:",code)

if __name__=="__main__":
    game()