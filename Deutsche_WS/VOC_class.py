'''
Class containing the personal list and related functions
'''

import random
import re

field_sep = "[,:;\t]"

# WS List class
class VOC():
    def __init__(self, fout="Deutsche_WS/list_files/my_list_example.txt"):
        '''
        List of words
        --> my_list_example.txt: list of words with relevant fields store in 6th line
        '''

        self.fout = fout

        # my_list in dictionary format
        self.my_dict = []
        # my_list in list format
        self.my_list = []

        # initialize list
        # ------------------------------------------

        with open(self.fout, 'r') as file:

            Lines = file.readlines()
            tmp_str = Lines[6][2:-1] # remove \n

            # store keys
            self.keys = re.split(field_sep,tmp_str)

            # store words
            for line in Lines[8:]:

                # initialize dict for my_dict
                word = {}
                line = re.split(field_sep, line)

                # remove new line character /n
                line = line[:-1]

                # store word in my_list
                self.my_list.append(line)

                # check for format issue
                if not line: # look for empty line
                    break
                if len(line) != len(self.keys): # look for format issue at specific line
                    raise ValueError('The format is incorrect for the line containing the word {}'.format(line[0]))

                for key, field in zip(self.keys, line):
                    word[key] = field
                self.my_dict.append(word)
        del tmp_str

        self.extra_key = []
        self.extra_list = []

    def change_list(self, fout):
        '''
        Use an other stored list of vocabulary
        If not present, creates it

        :param: name of the file
        :return:
        '''

        fout = 'list_files/'+fout

        #if fout.exist():
        #else:



    def add_extra_list(self, f_extra, key):
        # todo: add possibility to change already stored world
        '''
        add additional list of words from file with given keys
        :return:
        '''

        # store new key related to additional list
        self.extra_key.append(key)

        # store words in tmp_list
        tmp_list = []
        with open(f_extra, 'r') as file:

            lines = file.readlines()

            # store words
            for line in lines:

                word = {}
                line = re.split(field_sep, line)

                # check for format issue
                if len(line) != len(key):
                    raise ValueError('The format is incorrect for the line containing the word {}'.format(line[0]))

                for k,field in zip(key, line):
                    word[k] = field
                tmp_list.append(word)

        # add new list to extra_list
        self.extra_list.append(tmp_list)
        del tmp_list


    def add_word(self, add_word):
        '''
        Update my_list_example.txt with a new word and related keys,
        or add one or more additional keys to an already stored word

        :param add_word: list of keys to add to my_list.
                         [word, translation, etc]
        '''

        # check if word is already stored
        # --------------------------------

        stored = False
        for stored_word in self.my_dict:
            if add_word[0] in stored_word[self.keys[0]]:
                stored = True
                break

        if not stored:

            # print new word in my_list_example.txt
            with open(self.fout, 'a') as file:
                file.write(','.join(add_word)+','+'\n')

            # append my_list
            self.my_list.append(add_word)

            # append my_dict
            word = {}
            for k,e in zip(self.keys, add_word):
                word[k] = e
            self.my_dict.append(word)

    def print_rand(self):
        '''
        Print random word and ask for translation
        '''

        tot_list = self.my_dict + self.extra_list

        return random.choice(tot_list)


if __name__ == '__main__':

    WS = VOC()
    print(len(WS.my_dict[0]))
    print(WS.my_dict)
    WS.add_word(["leichtsinnig", "inconsidéré", "adjectiv", "", "", "", "", ""])
    print(WS.my_dict[-1])
    print(WS.my_list[-1])
