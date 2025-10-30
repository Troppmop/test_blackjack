from core import game_logic, deck

if __name__ == "__main__":
    game_deck = deck.build_standard_deck()
    shuffled_deck = deck.shuffle_by_suit(game_deck)

    player = {'hand':[]}
    dealer = {'hand':[]}

    game_logic.run_full_game(game_deck,player, dealer)