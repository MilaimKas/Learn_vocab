import WS_class
import random

print('Initialization, wait a few seconds ...')
word_list = WS_class.WS()
var = input(print("Do you want to test your skills (type 1) or add new words (type 2) "))

# Exercise
if var == 1:
   # random test F --> D
   print(random.choice(word_list))
   # random test D --> F

# Add new words
if var == 2:

