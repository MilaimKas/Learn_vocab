import random
import json

# keys
w = "word"
t  = "Theme"
a  = "artikel"
ub  = "Übersetzung französich"
s  = "Synonyme"
ex  = "Beispiel"
plu  = "plural"

# WS List class
class WS():
    def __init__(self):
        '''
        List of words
        --> my_list.txt: list of dictionary variables containing keys
        --> extra_list: simple list of words (with article)
        '''

        # initialize list of words found in my_list.txt
        self.my_list = []
        with open('my_list.txt', 'r') as file:
            Lines = file.readlines()
            for line in Lines:
                self.my_list.append(json.loads(line.strip()))

        self.extra_list = []

    def init_mylist(self):
        """
        re-initialize my_list (if new words have been added for example)
        :return:
        """
        self.my_list = []
        with open('my_list.txt', 'r') as file:
            Lines = file.readlines()
            for line in Lines:
                self.my_list.append(json.loads(line.strip()))

    def add_extra_list(self,file):
        '''
        add additional list of words from file
        :return:
        '''

        with open(file) as f:
            self.extra_list.extend([line.rstrip() for line in f])


    def add_word(self,word,item=None):
        '''
        Update my_list.txt with a new word and related keys,
        or add one or more additional keys to an already stored word

        :param word: word to had to the list
        :param kwargs: additional, optional, keys and item (must be a list of tuple)
        '''

        # check if word is already stored
        for stored_word in self.my_list:
            if word in stored_word["word"]:
                print('This word is already stored with the following related keys: ')
                print(stored_word)
                #print('Do you wish to add a new key (yes/no) ?')
                #if input() == 'yes':
            # write new line in my_list.txt
            else:
                new_word = '{'+'\"word\": \"{}\"'.format(word)
                if item is not None:
                    for key, it in item:
                        new_word += ', '+'\"{}\": \"{}\"'.format(key, it)
                    new_word += '}'
                    with open('my_list.txt', 'a') as file:
                        file.write(str(new_word)+'\n')
                break

    def print_rand(self):
        # todo: different format between my_list and extra_list
        '''
        Print random word in german (or french) and asks for translation
        '''

        tot_list = self.my_list+self.extra_list

        return random.choice(tot_list)


if __name__ == '__main__':

    WS = WS()
    print(len(WS.my_list[0]))
    print(WS.my_list)
    WS.add_word("leichtsinnig", [('translation','inconsidéré'), ('synonyme', 'fahrlässig')])
