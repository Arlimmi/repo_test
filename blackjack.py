import random, time

# Representing Card Deck
cards = [
   '2',
   '3',
   '4',
   '5',
   '6',
   '7',
   '8',
   '9',
   '10',
   'Jack',
   'Queen',
   'King',
   'Ace'
]

# Random Pull of 1 & 2 cards
dealer_start_cards = random.sample(cards, k=1)
player_start_cards = random.sample(cards, k=2)

# Calculates sum of cards
def current_score(hand):
    current_player = 0

    for cards in hand:
        if cards == "Jack" or cards == "Queen" or cards == "King":
            current_player += 10
        elif cards == "Ace":
            current_player += 11
        else:
            current_player += int(cards)

    return current_player

# Introduction & First Hand
def first_hand(current_player):
    print(
        "---------------------------------\n"
        "Welcome to Sahel's Blackjack!\n"
        "---------------------------------"
        )
    time.sleep(1)

    print("The Dealer pulls: " + " & ".join(dealer_start_cards))

    time.sleep(2)

    print("You pull: " + " & ".join(player_start_cards))
    print(f"\nYour Total is {current_player}\n")

# Main Code
def main():
    current_player = current_score(player_start_cards)
    current_dealer = current_score(dealer_start_cards)
    first_hand(current_player)

    while current_player <= 21:
        time.sleep(3)
        print(
        '\nHIT OR STAY?\n'
        '----------------------------------'
        )
        
        hit_stay = str(input('Would you like to hit or stay?: '))

        # If player hits
        if hit_stay == "h" or hit_stay == "hit":
            time.sleep(1)
            pull_card = random.sample(cards, k=1)
            current_player += int(current_score(pull_card))

            print("\nYou pull: " + " & ".join(pull_card)+ "\n")
            print(f"Your Total is {current_player}\n")

        # If player stays
        elif hit_stay == "s" or hit_stay == "stay":
            while current_dealer < 17:
                time.sleep(2)
                pull_card = random.sample(cards, k=1)
                current_dealer += int(current_score(pull_card))
            
                print("\nDealer pull: " + " & ".join(pull_card))
                print(f"Dealer Total is {current_dealer}")   
            break

        # Wrong input
        else:
            print("Please enter h or s.\n")
            continue   
            
    # Outcomes
    if current_dealer > 21:
        time.sleep(2)
        print("\nDealer busts! You win!")
    elif current_player > 21:
        time.sleep(2)
        print("\nYou bust!")
    elif current_player > current_dealer:
        time.sleep(2)
        print("\nYou win!")
    elif current_player < current_dealer:
        time.sleep(2)
        print("\nYou lost!")
    else:
        time.sleep(2)
        print("\nIt's a tie!")

# Execute Code
main()