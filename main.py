def printCard(suit_input, rank_input):
    top_left_corner = "╔"
    top_right_corner = "╗"
    bottom_left_corner = "╚"
    bottom_right_corner = "╝"
    vertical_edge = "║"
    horizontal_edge = "═"

    card_width = 11
    card_height = 9

    club = "♣"
    diamond = "♦"
    heart = "♥"
    spade = "♠"
    default_suit = "♥"

    suit = None
    rank = None

    if suit_input == "club":
        suit = club
    elif suit_input == "diamond":
        suit = diamond
    elif suit_input == "heart":
        suit = heart
    elif suit_input == "spade":
        suit = spade
    else:
        suit = default_suit

    try:
        rank_value = int(rank_input)
        if 2 <= rank_value <= 10:
            rank = rank_input
        elif rank_value == 11:
            rank = 'J'
        elif rank_value == 12:
            rank = 'Q'
        elif rank_value == 13:
            rank = 'K'
        else:
            rank = 'A' 
    except ValueError:
        if rank_input == "ace" or rank_input == "a":
            rank = 'A'
        elif rank_input == "jack" or rank_input == "j":
            rank = 'J'
        elif rank_input == "queen" or rank_input == "q":
            rank = 'Q'
        elif rank_input == "king" or rank_input == "k":
            rank = 'K'
        else:
            rank = 'A' 

    print(top_left_corner + horizontal_edge * card_width + top_right_corner)

    for i in range(card_height - 2):  
        if i == 0:  
            print(vertical_edge + ' ' + rank + ' ' * (card_width - 2) + vertical_edge)
        elif i == (card_height - 2) // 2: 
            print(vertical_edge + ' ' * ((card_width - 1) // 2) + suit + ' ' * ((card_width - 1) // 2) + vertical_edge)
        elif i == card_height - 3:  
            print(vertical_edge + ' ' * (card_width - 2) + rank + ' ' + vertical_edge)
        else:  
            print(vertical_edge + ' ' * card_width + vertical_edge)

    print(bottom_left_corner + horizontal_edge * card_width + bottom_right_corner)


another_card = True

while another_card == True:
    suit_input = input("Enter suit (club, diamond, heart, spade): ").lower().strip()
    rank_input = input("Enter rank (2-10, Jack, Queen, King, Ace): ").lower().strip()

    printCard(suit_input, rank_input)

    continue_game = input("Create another card? Y/N: ").lower().strip()

    if continue_game == 'n':
        break
    else:
        continue
