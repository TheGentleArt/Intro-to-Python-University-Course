# Justin Williams
# Assignment 02
# EPD 455: Python for Applications in Engineering
# 2022-09-25
#
# Problem 6
#    The txt file here contains the first 500 lines of the famous book “The Time Machine” by H.G.Wells.
#    Write a python program to find the number of occurances of the 10 most common words in these 500 lines. 
#    Print these 10 words along with the number of times they occur in seperate lines as shown below. 
#    Make sure to strip all punctuations and convert all the words to lowercase to get an accurate count. 
#    Feel free to google how to open and read words from a file. 
#    Submit the script task6.py on canvas.
#    Test Case :
#    $ python3 t a s k 6 . py
#    c o n s i d e r a b l e − 285 t i m e s
#    t h e − 108 t i m e s
#    a − 103 t i m e s
#    maybe − 93 t i m e s
#    time − 68 t i m e s
#    b e c a u s e − 66 t i m e s
#    why − 57 t i m e s
#    i n − 56 t i m e s
#    i − 51 t i m e s
#    t h a t − 51 t i m e s
#
# "here" hyperlink goes to: 

# number_of_words = 0
# with open("sample.txt", "r") as myfile:
#     file_contents = myfile.read()
#     count = 0
#     for line in file_contents:
#         word = line.split()
#         count += len(word)
#     print("Total number of words: " + str(count))

alphabetical="abcdefghijklmnopqrstuvwxyz"
alphabetical = alphabetical.lower() + alphabetical.upper()




myfile = open('task6file.txt', 'r')
file_contents = myfile.readlines() # creates an list with each line being a different element

mod_file_contents = []

for line in file_contents:
    mod_file_contents.append(line.strip())
    
stringy = mod_file_contents[144:152]

    
    
    

    
