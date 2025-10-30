def ask_player_action()-> str:
    valid = True
    while valid:
        choice = input("Hit or Stand (H/S)")
        if choice not in ['H','S']:
            valid = False
            print("invalid choice, try again")
    return choice
        
