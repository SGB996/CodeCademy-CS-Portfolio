import random

cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

# index = random.choice(list(cards.keys()))
# print(index)
# print(cards[index])


player = input('Enter player name: ')

def blackjack():
    hand = {}
    while len(hand) < 2:
        index = random.choice(list(cards.keys()))
        hand.update({index: cards[index]})
    print('Your hand is: ', list(hand.keys()))
    print('Your hand sum is: ', sum(list(hand.values())))
    play = input('Do you want to keep playing? Y/N: ')
    if play == 'Y':
        index = random.choice(list(cards.keys()))
        hand.update({index: cards[index]})
        suma = sum(list(hand.values()))
        if suma > 21:
            print('You lost your sum is :', suma)
        elif suma < 21:
            print('Your hand sum is: ', suma)
        print(hand)
    newSuma = sum(list(hand.values()))
    if newSuma > 21:
        print('You lost your sum is :', newSuma)
    if newSuma < 21:
        play = input('Do you want to keep playing? Y/N: ')
        if play == 'Y':
            index = random.choice(list(cards.keys()))
            hand.update({index: cards[index]})
            newSuma = sum(list(hand.values()))
            print('Your hand sum is: ', newSuma)
        else: 
            print('You stopped and your hand sum is: ', newSuma)





if player != '':
    print(blackjack())


