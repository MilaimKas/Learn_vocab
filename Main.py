'''

todo: make display list for add new word option
todo: Make my_list a table with column corresponding to keys, with WS class creating list of dict
todo: google translate option
todo:

'''

import WS_class
import PySimpleGUI as sg

# stop command
exit = ['exit','stop','quit']

# initializing vocabulary list and class
#print('Initialization, wait a few seconds ...')
WS = WS_class.WS()
keys = WS.keys
#print("Do you want to test your skills (type 1) or add new words (type 2) ")
#var = input()
var = None

# initializing GUI window
sg.theme('DarkAmber')   # Add a touch of color
# ----- Full layout -----
layout = [
        [sg.Text("TEST YOUR SKILLS")],
        [sg.Button("Generate word", key="-generate-"), sg.In(enable_events=True, key="-word_to_translate-")],
        [sg.Text("Enter translation: "), sg.InputText(), sg.Button('Check', key="-Check-")],
        [sg.HSeparator()],
        [sg.Text("ADD A NEW WORD TO YOUR PERSONAL LIST")],
        [sg.Text("New word: ", key="-displayed_key-"), sg.InputText(key="-new_word-", enable_events=True)],
        [sg.Button('ADD', key="-add_word-")],
        [sg.Cancel("Exit")],
]
# Create the window
window = sg.Window("Deutshes Wortschatz", layout)

word = None
# Event loop
while True:

    # read action on the window
    event, values = window.read()

    # ---- check event ----

    # Translate

    if event == "-generate-":
        # print random word present in WS.list
        word = WS.print_rand()
        window["-word_to_translate-"].update(word[keys[0]])

    if event == "-Check-":
        if word is None:
            sg.popup("You have to generate a word to translate before given a translation !!")
        else:
            if values[0] in word[keys[3]]:
                sg.popup('Correct !')
            else:
                text_out = word[keys[3]]
                #text_out = ''
                #for i in word:
                #    text_out += '{}, -> {} \n'.format(i, word[i])
                sg.popup('Incorrect, the translation is: \n'+text_out)

    # Add word

    # close window
    if event == sg.WIN_CLOSED or event == "Exit":
        break

window.close()

