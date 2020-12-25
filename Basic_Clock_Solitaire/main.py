'''
Python Lab 6: Clock Solitaire FINAL
Mehmet Yilmaz
10-18-2018
CSCI101
*Here is a Clock Solitaire card game solver
'''

import random
import time

a = [['  ', ' A', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' X', ' J', ' Q', ' K'], ['4:', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**'],  ['3:', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**'], ['2:', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**'], ['1:', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**', '**']]
counter = 0
p = 13
deck = []

def make_deck():
    global deck
    Suits = ['H','S','D','C']
    Ranks = ['A','2','3','4','5','6','7','8','9','X','J','Q','K']
    for i in range(0,4):
        for w in range(0,13):
            answer = str(Suits[i] + Ranks[w])
            deck.insert(0,answer)
    return deck

def deal_cards(deck, x, y):
    list = []
    one = []

    # PLEASE READ, Here is the seed value for random that will lead you to winning the game:
    # h = 4
    # random.seed(h)
    # The Seed is 4 !!!
    
    random.shuffle(deck)
    for i in range(0,len(deck)):
        if(i % 4 != 0):
            one.insert(0,deck[i])
        elif(i % 4 == 0):
            list.insert(0,one)
            one = []
            one.insert(0,deck[i])
    one = [deck[len(deck)-1], deck[len(deck)-2], deck[len(deck)-3], deck[len(deck)-4]]
    list.insert(0,one)
    del list[-1]
    return list

list10 = [1]
def show_deck(b, x):
    global counter
    x = x + 1
    list = []
    list1 = []
    list2 = []
    list3 = []
    global list10
    global p
    for i in range(13):
        list.insert(i, b[i][0])
    list.insert(0, '4:')
    for i in range(13):
        list1.insert(i, b[i][1])
    list1.insert(0, '3:')
    for i in range(13):
        list2.insert(i, b[i][2])
    list2.insert(0, '2:')
    for i in range(13):
        list3.insert(i, b[i][3])
    list3.insert(0, '1:')
    list10.insert(0,list3)
    list10.insert(0,list2)
    list10.insert(0,list1)
    list10.insert(0,list)
    list10 = list10
    for t in range(5):
        if(a[t][x] == '**'):
            a[t][x] = list10[t-1][x]
            for i in range(5):
                print(" ".join(a[i]))
            if(list10[t-1][x] == 'SK' or list10[t-1][x] == 'CK' or list10[t-1][x] == 'HK' or list10[t-1][x] == 'DK'):
                counter += 1
            p_value(list10, t-1, x)
            a[t][x] = '  '
            break
    print('King count:',counter)

def p_value(list10, t, x):
    global p
    if(list10[t][x][1:] == 'A'):
        b = 1
    elif(list10[t][x][1:] == 'X'):
        b = 10
    elif(list10[t][x][1:] == 'J'):
        b = 11
    elif(list10[t][x][1:] == 'Q'):
        b = 12
    elif(list10[t][x][1:] == 'K'):
        b = 13
    else:
        b = int(list10[t][x][1:])
    p = b

def give():
    global p
    return p-1

def main(y, z):
    global counter, p, l
    deck = make_deck()
    deck = deal_cards(deck, y, z)
    for i in range(4):
        for c in range(14):
            time.sleep(0.5)
            p = give()
            if(counter != 4):
                show_deck(deck, p)
                print(' ')
            elif(counter == 4):
                break

main(0,0)