from art import logo
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6 ,7 , 8, 9, 10, 10, 10, 10]
    return random.choice(cards)



play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play_game == 'y':
    player_cards = []
    cpu_cards = []
    print(logo)

    # deal first round
    cpu_cards.append(deal_card())
    player_cards.append(deal_card())
    cpu_cards.append(deal_card())

    new_round = 'y'
    while new_round == 'y':
        player_cards.append(deal_card())

        score = sum(player_cards)
        if score > 21:
            break
            
        # Show round results
        print(f"\n\tYour cards: {player_cards}, current score: {score}")
        print(f"\tComputer's first card: {cpu_cards[0]}\n")

        # ask for another round
        new_round = input("Type 'y' to get another card, type 'n' to pass: ")

    # Cpu turn
    cpu_score = sum(cpu_cards)

    while(cpu_score < 17):
        cpu_cards.append(deal_card())
        cpu_score = sum(cpu_cards)


    # End game 
    print(f"\n\tYour final hand: {player_cards}, final score: {score}")
    print(f"\tComputer's final hand: {cpu_cards}, final score: {cpu_score}\n")

    if score > 21:
        print("\tYou wentover, you loose 😤")
    elif cpu_score > 21:
        print("\tOponent went over, you win 😁")
    elif score < cpu_score:
        print("\tYou loose 😤")
    elif score > cpu_score:
        print("\tYou win 😁")
    else:
        print("\tIt's a draw!!")

    play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")


print("\nSee you next time")