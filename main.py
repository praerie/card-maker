def printCard(suit_input):
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
    empty_suit = " "

    suit = None

    if suit_input == "club":
        suit = club
    elif suit_input == "diamond":
        suit = diamond
    elif suit_input == "heart":
        suit = heart
    elif suit_input == "spade":
        suit = spade
    else:
        suit = empty_suit

    print(top_left_corner + horizontal_edge * card_width + top_right_corner)

    for i in range(card_height - 2):  
        if i == 0:  
            print(vertical_edge + " A" + ' ' * (card_width - 2) + vertical_edge)
        elif i == (card_height - 2) // 2: 
            print(vertical_edge + ' ' * ((card_width - 1) // 2) + suit + ' ' * ((card_width - 1) // 2) + vertical_edge)
        elif i == card_height - 3:  
            print(vertical_edge + ' ' * (card_width - 2) + "A " + vertical_edge)
        else:  
            print(vertical_edge + ' ' * card_width + vertical_edge)

    print(bottom_left_corner + horizontal_edge * card_width + bottom_right_corner)

suit_input = input("Enter your suit (club, diamond, heart, spade): ").lower()
printCard(suit_input)