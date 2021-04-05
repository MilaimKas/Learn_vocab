import WS_class
import random
import sys

# stop command
exit = ['exit','stop','quit']
# list of keys
keys = ["translation","synonyme","article","theme"]

# initializing
print('Initialization, wait a few seconds ...')
WS = WS_class.WS()
print("Do you want to test your skills (type 1) or add new words (type 2) ")
var = input()

# Exercise
if var == '1':
   # random test F --> D
   print('press enter to start')
   while input() not in exit:
       word = WS.print_rand()
       print('Translate the word: ',word["word"])
       if input() in word[keys[0]]:
           print('Correct !')
       else:
           print('Incorrect, last chance')
           if input() in word[keys[0]]:
               print('Correct !')
           else:
               print('Incorrect')
               print('The correct translation is: ', word[keys[0]])

   # random test D --> F

# Add new words
if var == '2':
    tmp = []
    print('Word to add')
    w = input()
    for key in keys:
        print(key)
        tmp.append((key,input()))

    WS.add_word(w,tmp)

else:
   print("Do you want to test your skills (type 1) or add new words (type 2) ")

