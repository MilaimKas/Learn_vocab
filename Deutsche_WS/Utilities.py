'''
List of used function in Main

'''

# numpy
import duden
import numpy as np
# GUI
import PySimpleGUI as sg
# nice table
from tabulate import tabulate
# french conjugation package
from mlconjug3 import Conjugator
# import german duden
from duden import get

def conjugate_fr(verb):
    # todo: add color and participe présent
    '''
    print formated text with conjugation table

    :param verb:
    :return:
    '''

    # List of table for each tense
    table = []

    # Conjugate verb
    w = Conjugator(language='fr').conjugate(verb)

    # Convert to numpy array and change personal noun
    w = w.iterate()
    w_arr = np.full((11, 7, 2), None)   # 11 tenses, 6 personnel noun and tense form

    # w_arr[k, l, 2]
    k = 1  # counter for w_arr

    # Infinitif
    w_arr[0, 1, 0] = w[0][1]
    w_arr[0, 1, 1] = w[0][2]
    # Ind -> Sub
    for i in range(1, 42, 6):
        # tense name
        tmp = list
        w_arr[k, 0, 0] = "{:-<18}".format('')
        w_arr[k, 0, 1] = "{:-<25}".format(w[i][0]+' '+w[i][1])
        # personal prenoun
        w_arr[k, 1, 0] = "{:<18}".format('je')
        w_arr[k, 2, 0] = "{:<18}".format('tu')
        w_arr[k, 3, 0] = "{:<18}".format('il/elle/on')
        w_arr[k, 4, 0] = "{:<18}".format('nous')
        w_arr[k, 5, 0] = "{:<18}".format('vous')
        w_arr[k, 6, 0] = "{:<18}".format('ils/elles/ont')
        # tense form
        for j in range(6):
            w_arr[k, j+1, 1] = "{:<25}".format(w[i+j][3])
        tmp = np.where(w_arr[k, :, :] is None, ' ', w_arr[k, :, :])
        table.append(tabulate(tmp, tablefmt='plain', numalign="center"))
        k += 1
    # Imp présent
    w_arr[k, 0, 0] = "{:-<18}".format('')
    w_arr[k, 0, 1] = "{:-<25}".format(w[43][1])
    w_arr[k, 1, 0] = "{:<18}".format("(tu)")
    w_arr[k, 2, 0] = "{:<18}".format("(nous)")
    w_arr[k, 3, 0] = "{:<18}".format("(vous)")
    for j in range(3):
        w_arr[k, j+1, 1] = "{:<25}".format(w[43+j][3])
    tmp = np.where(w_arr[k, :, :] is None, ' ', w_arr[k, :, :])
    table.append(tabulate(tmp, tablefmt='plain', numalign="center"))
    k += 1
    # participe présent
    w_arr[k, 0, 0] = w[46][1]
    w_arr[k, 0, 1] = w[46][2]
    part_pres = w_arr[k, 0, 0]+' '+w_arr[k, 0, 1]
    k += 1
    # participe passé
    w_arr[k, 0, 0] = "{:-<18}".format('')
    w_arr[k, 0, 1] = "{:-<25}".format(w[47][1])
    w_arr[k, 1, 0] = "{:<18}".format("masculin singulier")
    w_arr[k, 2, 0] = "{:<18}".format("masculin pluriel")
    w_arr[k, 3, 0] = "{:<18}".format("féminin singulier")
    w_arr[k, 4, 0] = "{:<18}".format("féminin pluriel")
    for j in range(1, 5):
        w_arr[k, j, 1] = "{:<25}".format(w[46+j][3])
    tmp = np.where(w_arr[k, :, :] is None, ' ', w_arr[k, :, :])
    table.append(tabulate(tmp, tablefmt='plain', numalign="center"))

    # formated sg window
    # participe présent
    col = []
    k = 0
    for i in range(3):
        row = []
        for j in range(3):
            row.extend([sg.Text(table[k], font='Courier', text_color='white'), sg.VSeparator(color='white')])
            k += 1
        col.append(row)
        col.append([sg.HSeparator(color='white')])

    return col

def conjugate_de(verb):

    # use duden
    w = duden.get(verb)

    w_arr = np.full((6, 7, 2), None)   # 5 tenses, 6 personnel noun and tense form
    table = []

    # Infinitiv
    w_arr[0, 1, 0] = 'Infinitiv mit zu'
    w_arr[0, 1, 1] = w.grammar(duden.INFINITIV_MIT_ZU)

    prasens = w.grammar(duden.PRASENS)
    prateritum = w.grammar(duden.PRATERITUM)

    # Indikativ prasens
    w_arr[1, 0, 0] = "{:-<18}".format('')
    w_arr[1, 0, 1] = "{:-<25}".format('INDIKATIV'+' '+'PRASENS')
    tmp = prasens[0::3]
    for j in range(6):
        form = tmp[j].split()
        # personal prenoun and form
        w_arr[1, j+1, 0] = "{:<18}".format(form[0])
        w_arr[1, j+1, 1] = "{:<25}".format(form[1])
    tmp = np.where(w_arr[1, :, :] is None, ' ', w_arr[1, :, :])
    table.append(tabulate(tmp, tablefmt='plain', numalign="center"))

    # Indikativ prateritum
    w_arr[2, 0, 0] = "{:-<18}".format('')
    w_arr[2, 0, 1] = "{:-<25}".format('INDIKATIV' + ' ' + 'PRATERITUM')
    tmp = prateritum[0::2]
    for j in range(1, 6):
        form = tmp[j].split()
        # personal prenoun and form
        w_arr[2, j+1, 0] = "{:<18}".format(form[0])
        w_arr[2, j+1, 1] = "{:<25}".format(form[1])
    tmp = np.where(w_arr[2, :, :] is None, ' ', w_arr[2, :, :])
    table.append(tabulate(tmp, tablefmt='plain', numalign="center"))

    # Konjunktiv I
    w_arr[3, 0, 0] = "{:-<18}".format('')
    w_arr[3, 0, 1] = "{:-<25}".format('KONJUNKTIV I' + ' ' + 'PRASENS')
    tmp = prasens[1::3]
    for j in range(1, 6):
        form = tmp[j].split()
        # personal prenoun and form
        w_arr[3, j+1, 0] = "{:<18}".format(form[0])
        w_arr[3, j+1, 1] = "{:<25}".format(form[1])
    tmp = np.where(w_arr[3, :, :] is None, ' ', w_arr[3, :, :])
    table.append(tabulate(tmp, tablefmt='plain', numalign="center"))

     # Konjunktiv II
    w_arr[4, 0, 0] = "{:-<18}".format('')
    w_arr[4, 0, 1] = "{:-<25}".format('KONJUNKTIV II' + ' ' + 'PRASENS')
    tmp = prateritum[1::2]
    for j in range(1, 6):
        form = tmp[j].split()
        # personal prenoun and form
        w_arr[4, j+1, 0] = "{:<18}".format(form[0])
        w_arr[4, j+1, 1] = "{:<25}".format(form[1])
    tmp = np.where(w_arr[4, :, :] is None, ' ', w_arr[4, :, :])
    table.append(tabulate(tmp, tablefmt='plain', numalign="center"))

    # Imperativ
    w_arr[5, 0, 0] = "{:-<18}".format('')
    w_arr[5, 0, 1] = "{:-<25}".format('IMPERATIV' + ' ' + 'PRASENS')
    tmp = prasens[2::3]
    w_arr[5, 1, 0] = "{:-<18}".format('')
    w_arr[5, 4, 0] = "{:-<18}".format('')
    w_arr[5, 1, 1] = "{:<25},{}!".format(tmp[1].split()[0], tmp[1].split()[3])
    w_arr[5, 4, 1] = "{:<25}!".format(tmp[4].split()[0])
    tmp = np.where(w_arr[5, :, :] is None, ' ', w_arr[5, :, :])
    table.append(tabulate(tmp, tablefmt='plain', numalign="center"))

    # formated sg window
    col = []
    k = 0
    for i in range(2):  # row
        row = []
        for j in range(2):  # column
            row.extend([sg.Text(table[k], font='Courier', text_color='white'), sg.VSeparator(color='white')])
            k += 1
        col.append(row)
        col.append([sg.HSeparator(color='white')])

    return col

if __name__ == '__main__':
    conjugate_de('laufen')


