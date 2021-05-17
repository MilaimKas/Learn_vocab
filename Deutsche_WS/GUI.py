'''
Main program

additional features to look at:
- pattern package: https://stackabuse.com/python-for-nlp-introduction-to-the-pattern-library/
- German semantic library: https://pypi.org/project/pygermanet/
                        and https://gist.github.com/amotl/ad5ecda4579ad60bb6497b7ddabc8ad0
- mlconjug package: https://pypi.org/project/mlconjug/
- duden: https://github.com/radomirbosak/duden/blob/master/docs/usage.md

Needed packages: PySimpleGUI, tabulate, googletrans, verbecc3 (scikit-learn)
'''

from Deutsche_WS import VOC_class
from Deutsche_WS.Utilities import conjugate

# GUI
import PySimpleGUI as sg

# nice table
from tabulate import tabulate

# google translate package
from googletrans import Translator

def Main():

##########################################
# initializing vocabulary list and class
##########################################

    WS = VOC_class.VOC()
    keys = WS.keys

##############################################
# Conjugation function and languages
##############################################

    lang_src = 'german'
    lang_dest = 'french'

############################
# initializing GUI window
############################

    sg.theme('DarkAmber')   # Add a touch of color

# ----- Full layout -----
    new_word_layout = []
    for k in keys:
        new_word_layout.append([sg.Text(k+' :', size=(10, 1)), sg.InputText(key=k)])

    layout = [
            [sg.Menu([['&Source language', ['&french', '&german']],
                      ['&About']])],
            [sg.Text("TEST YOUR SKILLS", size=(35, 1), justification='center', relief=sg.RELIEF_RIDGE)],
            [sg.Button("Generate word", key="-generate-"), sg.In(enable_events=True,
                                                                 key="-word_to_translate-", size=(35, 1))],
            [sg.Text("Enter translation: "), sg.InputText(size=(35, 1), key="-translation-"), sg.Button('Check',
                                                                                                    key="-check-")],
            [sg.Text('', key='-answer-', size=(35, 1))],
            [sg.Text('')],
            [sg.Text("GET INFORMATION", size=(35, 1), justification='center', relief=sg.RELIEF_RIDGE)],
            [sg.Button("ASK GOOGLE", enable_events=True, key='-google-'), sg.In(key='-google_to_translate-', size=(35, 1))],
            [sg.Text('', key='-google_answer-', size=(35, 1))],
            [sg.Button("CONJUGATE", enable_events=True, key='-conjugate-'),
                      sg.In(key='-to_conjugate-', size=(35, 1))],
            [sg.Text('')],
            [sg.HSeparator()],
            [sg.Text('')],
            [sg.Text("ADD A NEW WORD TO YOUR PERSONAL LIST", size=(70, 1), justification='center', relief=sg.RELIEF_RIDGE)],
            [sg.Frame(title="New word to add", layout=new_word_layout), sg.Button('ADD', key="-add_word-")],
            [sg.Text('')],
            [sg.HSeparator()],
            [sg.Text('')],
            [sg.Text("DISPLAY YOUR PERSONAL LIST", size=(70, 1), justification='center', relief=sg.RELIEF_RIDGE)],
            [sg.Button('SHOW LIST', enable_events=True, key='-show_list-')],
            [sg.Text('')],
            [sg.HSeparator()],
            [sg.Text('')],
            [sg.Cancel("Exit")],
            ]
# Create the window
    window = sg.Window("French-German vocabulary", layout)

    word = None

#################
# Event loop
#################

    while True:

        # read action on the window
        event, values = window.read()

        # remove printed message
        window['-answer-'].update('')

        # Change source and destination language
        # ----------------------------------------
        if event == '&french':
            lang_src = 'french'
            lang_dest = 'german'
        if event == "&german":
            lang_src = 'german'
            lang_dest = 'french'

        # Show Readme file
        if event == '&About':
            text = open("../README.md", 'r').read()
            new_window = sg.Window('About',
                                   [
                                       [sg.Text(text, text_color='white')]
                                   ])
            while True:
                ev, val = new_window.read()
                if ev == sg.WIN_CLOSED:
                    break
            new_window.close()

        #  Translate from list
        # ----------------------------

        if event == "-generate-":
            # print random word present in WS.list
            word = WS.print_rand()
            window["-word_to_translate-"].update(word[keys[0]])

        if event == "-check-":
            if len(window["-word_to_translate-"].get()) == 0:
                sg.popup("You have to generate a word to translate before looking for the translation !!", title='Error')
            else:
                # check if translation is correct
                if values["-translation-"] in word[keys[1]]:
                    # print message bellow
                    window['-answer-'].update('Correct !')
                # check if synonym
                elif values["-translation-"] in word[keys[7]]:
                    # print messsage bellow
                    window['-answer-'].update('Correct but a better translation would be {}'.format(word[keys[1]]))
                else:
                    # print correct answer
                    text_out = word[keys[1]]+word[keys[7]]
                    window['-answer-'].update('Incorrect, the translation is/are: '+text_out)

        # Google translate
        # -----------------------

        if event == "-google-":
            if len(window["-google_to_translate-"].get()) == 0:
                sg.popup('You have to enter a word to translate !', title='Error')
            else:
                # translation is a class that contains several information in addition to the translation
                translation = Translator().translate(str(window['-google_to_translate-'].get())
                                       , src=lang_src, dest=lang_dest)
                # if text too long, print in external window
                if len(translation.text) < 20:
                    window['-google_answer-'].update('Translation: '+translation.text)
                else:
                    new_window = sg.Window('Translated text',
                                           [
                                               [sg.Text(translation.text)],
                                               [sg.Button('OK', key='-exit-')]
                                           ])
                    while True:
                        ev, val = new_window.read()
                        if ev == sg.WIN_CLOSED:
                            break
                        if ev == '-exit-':
                            break

        #
        # Conjugate
        # ------------------------

        if event == '-conjugate-':
            verb = window['-to_conjugate-'].get()
            if len(verb) == 0:
                sg.popup('You have to enter a verb to conjugate !', title='Error')
            else:
                # conjugate and return table of conjugation
                table_display = conjugate(verb, lang_dest)
                # open window with conjugation information
                sg.Window('Conjugation table of {}'.format(verb), layout=[[sg.Column(table_display)]]).read()



        # Add word to my_list
        # -----------------------

        if event == "-add_word-":

            # if no word is given
            if len(window[keys[0]].get()) == 0:
                sg.popup('At least a new word must be given in order to add a new item to your list !', title='Error')

            else:
                new_word = []
                for k in keys:
                    if len(window[k].get()) != 0:
                        new_word.append(window[k].get())
                    else:
                        new_word.append(" ")

                # Create new window for confirmation
                new_window = sg.Window('Add word',
                                   [
                                    [sg.Text('Add the following new word to your list ?')],
                                    [sg.Text(str(new_word))],
                                    [sg.Button('YES', key='-yes-'), sg.Button('NO', key='-no-')]
                                   ])
                # read event in new window
                while True:
                    ev, val = new_window.read()
                    if ev == sg.WIN_CLOSED:
                        break
                    if ev == '-yes-':
                        WS.add_word(new_word)
                        break
                    if ev == '-no-':
                        break
                new_window.close()

        # -- Show list --
        if event == "-show_list-":
            # todo: sort my_list alphabetically
            table = tabulate(WS.my_list, headers=keys, tablefmt='rst')
            sg.Window('My list of vocabulary in alphabetical order',
                      [[sg.Text(table, font='Courier', text_color='white')]]).read()

        # close window
        if event == sg.WIN_CLOSED or event == "Exit":
            break

    window.close()

