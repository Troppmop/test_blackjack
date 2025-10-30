import random

#global variables for code readability
ace_rank = 1
king_rank = 13
suite_list = ['S','D','H','C']
letter_rank_numbers = ['1','11','12','13']

#helper functions

#helper functions for build_standard_deck

#add cards with set numerical ranks and suites
def add_primitive_cards(empty_deck:list) -> list[dict]:
    for suite in range(len(suite_list)):
        for card_rank in range(ace_rank, king_rank + 1): #one is added to adjust for stopping value in the range function
            card = {
                'rank': str(card_rank), #one is added because we 
                'suite': suite_list[suite] #will be added in second loop
            }
            empty_deck.append(card)
    return empty_deck

#convert numerical ranks 1, 11,12,13 to letter ranks
def convert_to_letter_ranks(primitive_deck:list[dict])->list[dict]:
    for card in primitive_deck:
        match card['rank']:
            case '1':
                card['rank'] = 'A'
            case '11':
                card['rank'] = 'J'
            case '12':
                card['rank'] = 'Q'
            case '13':
                card['rank'] = 'K'
    regular_deck = primitive_deck
    return regular_deck

#helper functions for shuffle_by_suit

def validate_shuffle(deck: list[dict], i_index:int, j_index:int) ->bool:
    valid = False
    match deck[i_index]['suite']:
        case 'H':
            valid = j_index % 5 == 0
        case 'C':
            valid = j_index % 3 == 0
        case 'D':
            valid = j_index % 2 == 0
        case 'S':
            valid = j_index % 7 == 0

    if i_index == j_index:
        valid = False

    return valid

#required functions

#builds deck using helper functions
def build_standard_deck() -> list[dict]:
    empty_deck = []
    
    primitive_deck = add_primitive_cards(empty_deck)
    
    regular_deck = convert_to_letter_ranks(primitive_deck)

    return regular_deck


def shuffle_by_suit(deck: list[dict], swaps:int = 5000) ->list[dict]:
    deck_length = len(deck)

    for i in range(swaps):
        i = random.randint(0,51)
        j = random.randint(0,51)

        
        while validate_shuffle(deck,i,j):
            j = random.randint(0,51)
        
        temp_card = deck[i]
        deck[i] = deck[j]
        deck[j] = temp_card


    return deck

#test functions, will not run in main due to the __init__.py file
if __name__ == "__main__":
    deck = build_standard_deck()
    print(shuffle_by_suit(deck))    