# Justin Williams
# EPD 455: Python for Applications in Engineering
# Assignment 01
# 2022-09-17
#
# Problems statement for problem # 6 on homework:
#
#Write a python program that takes as input from the command line a character 
# ch and an int n and returns a character that is shifted in the alphabet n 
# positions. The program only deals in lower case letters of the English 
# alphabet; any other characters are illegal and should be ignored with an 
# error message and exit. You can assume that n will be a number between 
# -1000 and 1000. Also, the letters should be envisioned as being in a circular
# buffer. If letter z is shifted by 1 it would become a, while if shifted by 3 
# it would become c. By the same token, if a is shifted by -1 it becomes z.
# Submit the python file named task8.py to Canvas.
# Test case 1:
# $ python3 task8.py a 3
# d
# Test case 2:
# $ python3 task8.py a  -1
# z
# Test case 3:
# $ python3 task8.py B  
#Input value not supported. Program exiting...
#
# Could improve with changing letter chosen to letter_chosen = letter_chosen.lower().... but instructions were to exit with a warning...
alphabet = 'abcdefghijklmnopqrstuvwxyz'
chosen_letter = input('Enter your chosen lowercase letter here: ')
chosen_number = int(input('Enter your chosen integer away from your letter here: '))
if len(chosen_letter)>1:
    print('Pick only ONE letter...')
elif chosen_letter.isupper():
    print('Uppercase letters not supported...try again with lowercase...')
else:
    if chosen_number < 0:
        chosen_number_away = abs(chosen_number)%len(alphabet)*(-1)
    else:
        chosen_number_away = chosen_number%len(alphabet)
    chosen_letter_index = alphabet.index(chosen_letter)
    new_letter_index = (chosen_number_away + chosen_letter_index)%len(alphabet)
    new_letter = alphabet[new_letter_index]
    # print(chosen_number_away)
    print("The letter '",new_letter,"' is (",chosen_number,") letters away from the letter '",chosen_letter,"'.")

    
