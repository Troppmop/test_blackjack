from . import player_io
#helper functions

#helper function for calculate_hand_value
def calculate_card_value(card:dict) ->int:
    card_value = 0
    match card['rank']:
            case 'A':
                card_value = 11
            case 'J' | 'Q' | 'K':
                card_value = 10
            case _:
                card_value = int(card['rank'])
    return card_value

#required functions 

def calculate_hand_value(hand: list[dict]) -> int:
    hand_value = 0
    ace_count = 0
    
    #handle special ranks
    for card in hand:
        card_value = calculate_card_value(card)
        hand_value += card_value
        if card_value == 11:
            ace_count += 1
    #adjust aces for benefit of the hand value
    while hand_value > 21 and ace_count > 0:
        hand_value -= 10
        ace_count -= 1
    return hand_value


def deal_two_each(deck:list[dict], player: dict, dealer: dict)-> None:
    for i in range(2):
        player['hand'].append(deck.pop(0)) 
        dealer['hand'].append(deck.pop(0))

    print(f"Player hand value: {calculate_hand_value(player['hand'])}")
    print(f"Dealer hand value: {calculate_hand_value(dealer['hand'])}")

def dealer_play(deck:list[dict], dealer:dict)->bool: 
    while calculate_hand_value(dealer['hand']) < 17:
        dealer['hand'].append(deck.pop(0))
    
    hand_validity = calculate_hand_value(dealer['hand']) < 21
    
    return hand_validity

def run_full_game(deck:list[dict], player:dict, dealer:dict)-> None:
    deal_two_each(deck, player,dealer)
    player_stands = False
    while calculate_hand_value(player['hand']) < 21 and not player_stands:
        player_choice = player_io.ask_player_action()
        match player_choice:
            case 'H':
                print("Hitting")
                player['hand'].append[deck.pop(0)]
                print(calculate_hand_value(player['hand']))
            case 'S':
                player_stands = True
                print("Standing")
    player_hand_value = calculate_hand_value(player['hand'])
    dealer_hand_value = calculate_hand_value(dealer['hand'])
    if player_hand_value > dealer_hand_value:
        print(f"player wins, hand value is {player_hand_value}")
    elif dealer_hand_value > player_hand_value:
        print(f"dealer wins, hand value is {dealer_hand_value}")
    else: 
        print("tie")

#test functions
if __name__ == "__main__":
    import deck
    game_deck = deck.build_standard_deck()
    shuffled_deck = deck.shuffle_by_suit(game_deck)
    player = {'hand':[]}
    dealer = {'hand':[]}
    deal_two_each(game_deck, player, dealer)
    print(f"dealer hand valid: {dealer_play(game_deck,dealer)}", f", dealer hand value = {calculate_hand_value(dealer['hand'])}")

    