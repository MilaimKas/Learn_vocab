import random

# keys
aa = "word"
a  = "Theme"
b  = "artikel"
c  = "Übersetzung französich"
d  = "Synonyme"
e  = "Beispiel"
f  = "plural"

# WS List class
class WS():
    def __init__(self):
        '''
        List of words
        --> my_list: list of dictionary variables containing keys
        --> extra_list: simple list of words (with article)
        '''

        # initialize list of words found in my_list
        self.my_list = []
        with open('my_list') as f:
            self.my_list.append([line.rstrip() for line in f])

        self.extra_list = []

    def add_extra_list(self,file):
        '''
        add additional list of words from file
        :return:
        '''

        with open(file) as f:
            self.extra_list.append([line.rstrip() for line in f])


    def add_word(self,word,**kwargs):
        '''
        Update my_list with a new word and related keys,
        or add one or more additional keys to an already stored word

        :param word: word to had to the list
        :param kwargs: additional, optional, keys
        '''

        # check if word is already stored

        # if so, update keys and values
        # if not append my_list

        # Updates my_list in my_list.txt file


    def print_rand(self):
        '''
        Print random word in german and asks for translation
        '''

        tot_list = self.my_list.append(self.extra_list)
        print(random.choice(tot_list)['word'])

if __name__ == '__main__':

    WS = WS()
    print(len(WS.my_list[0]))
    print(WS.my_list)
    #WS.print_rand()
