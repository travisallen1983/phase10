"""
Creating a version of phase 10 to be played alone against a computer, 
or together with family and friends.

Players will get a set amount of cards and the remaining will be put in
the draw pile.
Players must be able to add more cards to their hand.
Players must be allowed to lay down their cards to match the phase they are on,
and to play on others laid down cards.
The game should tabulate all players scores after the last card of the winner of
the round is played. It should accumalate throughout the game.
A player must know the phase the are on, and the phase must change when they have
met the condtions for the phase.
The person who completes all 10 phases first is the winner. If two people
complete the 10th phase in the same round, the lower score wins.
    
    Set = cards of the same number.
    Run = cards in numerical order.
    
    Phase 1 – 2 sets of 3
    Phase 2 – 1 set of 3 and 1 run of 4
    Phase 3 – 1 set of 4 and 1 run of 4
    Phase 4 – 1 run of 7
    Phase 5 – 1 run of 8
    Phase 6 – 1 run of 9
    Phase 7 – 2 sets of 4
    Phase 8 – 7 cards of a color
    Phase 9 – 1 set of 5 and 1 set of 2
    Phase 10 – 1 set of 5 and 1 set of 3

"""
import random
import phase1
import phase2
import phase3
import phase4
import phase5
import phase6
import phase7
import phase8
import phase9
import phase10

#Get input for amount of players and the players names.
name_of_players = []
number_of_players = 0
need_player_info = True
while need_player_info == True:
    number_of_players = int(input("How many people are playing? "))
    if number_of_players >= 1 and number_of_players <= 4:
        for i in range(1, number_of_players + 1):
            player = input("What is the name of player " + str(i) + "? " )
            name_of_players.append(player.capitalize())
            i = i + 1
            need_player_info = False
    else:
        need_player_info = True

#Set players phases
all_phases = dict()
for i in range(number_of_players):
    player = name_of_players[i]
    phase = "PHASE 1"
    all_phases[player] = phase

print(all_phases)

#Set cards
cards = []
def set_cards():
    for i in range(1,13):
        for j in range(2):
            cards.append(str(i) + " RED")
            cards.append(str(i) + " GREEN")
            cards.append(str(i) + " BLUE")
            cards.append(str(i) + " YELLOW")
    for i in range(8):
        cards.append("WILD")
    for i in range(4):
        cards.append("SKIP")

#Create dictionary for play as key and cards as value
players_cards = dict()
#Add remaining cards to the draw pile
draw_pile = []
print(cards)

def shuffle_and_deal():
    #shuffle the cards   
    current_deck = cards
    print(current_deck)
    random.shuffle(current_deck)
    print(current_deck)
    #Deal cards
    for i in range(10):
        for j in range(number_of_players):
            player = name_of_players[j]
            print(player)
            current_card = current_deck[0]
            #card = cards[0]
            if player in players_cards.keys():
                players_cards[player].append(current_card)
            else:
                players_cards[player] = [current_card]
            #Remove dealt cards from master deck.
            print(len(current_deck))
            current_deck.remove(current_deck[0])
            print(len(current_deck))
    for card in current_deck:
        draw_pile.append(card)
            

def next_round(): 
    game_over = False
    while game_over == False:    
        for i in range(number_of_players): 
            print(name_of_players[i] + " it's you turn. You are on " + all_phases[name_of_players[i]])            
            print(players_cards.get(name_of_players[i]))
            new_list = sorted(players_cards.get(name_of_players[i]))
            for j in range(len(new_list)):
                print(new_list[j])
            choice = input("Do you want to draw a card or play from your hand? ")
            print(choice)
            if choice.upper() not in ('DRAW', 'PLAY', 'END'):
                input("Do you want to draw a card or play from your hand? ")
            if choice.upper() == "DRAW":
                print(type(draw_pile))
                print(draw_pile[0])
                players_cards[name_of_players[i]].append(draw_pile[0])
                draw_pile.remove(draw_pile[0])
            elif choice.upper() == "PLAY": 
                print(all_phases[name_of_players[i]])
                if all_phases[name_of_players[i]] == 'PHASE 1':
                    all_phases[name_of_players[i]] = phase1.phase_one(players_cards, name_of_players[i])
                   #Setting dictionary vlue for player to new phase
                    if all_phases[name_of_players[i]] == 'PHASE 1':
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]]
                    else:
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]][0]
                   #slicing list to only get the card values that follow the phase at index 0
                    new_list = all_phases[name_of_players[i]][1:]
                    print(all_phases)
                    if all_phases[name_of_players[i]] == 'PHASE 2':
                        print(name_of_players[i] + ' has completed the Phase 1!')
                        cards.clear()
                        draw_pile.clear()
                        for i in range(0, number_of_players):
                            del players_cards[name_of_players[i]]
                        set_cards()
                        shuffle_and_deal()
                elif all_phases[name_of_players[i]] == 'PHASE 2':
                    all_phases[name_of_players[i]] = phase2.phase_two(players_cards, name_of_players[i])
                   #Setting dictionary vlue for player to new phase
                    if all_phases[name_of_players[i]] == 'PHASE 2':
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]]
                    else:
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]][0]
                   #slicing list to only get the card values that follow the phase at index 0
                    new_list = all_phases[name_of_players[i]][1:]
                    print(all_phases)
                    if all_phases[name_of_players[i]] == 'PHASE 3':
                        print(name_of_players[i] + ' has completed the Phase 2!')
                        cards.clear()
                        draw_pile.clear()
                        for i in range(0, number_of_players):
                            del players_cards[name_of_players[i]]
                        set_cards()
                        shuffle_and_deal()
                elif all_phases[name_of_players[i]] == 'PHASE 3':
                    all_phases[name_of_players[i]] = phase3.phase_three(players_cards, name_of_players[i])
                   #Setting dictionary vlue for player to new phase
                    if all_phases[name_of_players[i]] == 'PHASE 3':
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]]
                    else:
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]][0]
                   #slicing list to only get the card values that follow the phase at index 0
                    new_list = all_phases[name_of_players[i]][1:]
                    print(all_phases)
                    if all_phases[name_of_players[i]] == 'PHASE 4':
                        print(name_of_players[i] + ' has completed the Phase 3!')
                        cards.clear()
                        draw_pile.clear()
                        for i in range(0, number_of_players):
                            del players_cards[name_of_players[i]]
                        set_cards()
                        shuffle_and_deal()
                elif all_phases[name_of_players[i]] == 'PHASE 4':
                    all_phases[name_of_players[i]] = phase4.phase_four(players_cards, name_of_players[i])
                   #Setting dictionary vlue for player to new phase
                    if all_phases[name_of_players[i]] == 'PHASE 4':
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]]
                    else:
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]][0]
                   #slicing list to only get the card values that follow the phase at index 0
                    new_list = all_phases[name_of_players[i]][1:]
                    print(all_phases)
                    if all_phases[name_of_players[i]] == 'PHASE 5':
                        print(name_of_players[i] + ' has completed the Phase 4!')
                        cards.clear()
                        draw_pile.clear()
                        for i in range(0, number_of_players):
                            del players_cards[name_of_players[i]]
                        set_cards()
                        shuffle_and_deal()
                elif all_phases[name_of_players[i]] == 'PHASE 5':
                    all_phases[name_of_players[i]] = phase5.phase_five(players_cards, name_of_players[i])
                   #Setting dictionary vlue for player to new phase
                    if all_phases[name_of_players[i]] == 'PHASE 5':
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]]
                    else:
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]][0]
                   #slicing list to only get the card values that follow the phase at index 0
                    new_list = all_phases[name_of_players[i]][1:]
                    print(all_phases)
                    if all_phases[name_of_players[i]] == 'PHASE 6':
                        print(name_of_players[i] + ' has completed the Phase 5!')
                        cards.clear()
                        draw_pile.clear()
                        for i in range(0, number_of_players):
                            del players_cards[name_of_players[i]]
                        set_cards()
                        shuffle_and_deal()
                elif all_phases[name_of_players[i]] == 'PHASE 6':
                    all_phases[name_of_players[i]] = phase6.phase_six(players_cards, name_of_players[i])
                   #Setting dictionary vlue for player to new phase
                    if all_phases[name_of_players[i]] == 'PHASE 6':
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]]
                    else:
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]][0]
                   #slicing list to only get the card values that follow the phase at index 0
                    new_list = all_phases[name_of_players[i]][1:]
                    print(all_phases)
                    if all_phases[name_of_players[i]] == 'PHASE 7':
                        print(name_of_players[i] + ' has completed the Phase 6!')
                        cards.clear()
                        draw_pile.clear()
                        for i in range(0, number_of_players):
                            del players_cards[name_of_players[i]]
                        set_cards()
                        shuffle_and_deal() 
                elif all_phases[name_of_players[i]] == 'PHASE 7':
                    all_phases[name_of_players[i]] = phase7.phase_seven(players_cards, name_of_players[i])
                   #Setting dictionary vlue for player to new phase
                    if all_phases[name_of_players[i]] == 'PHASE 7':
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]]
                    else:
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]][0]
                   #slicing list to only get the card values that follow the phase at index 0
                    new_list = all_phases[name_of_players[i]][1:]
                    print(all_phases)
                    if all_phases[name_of_players[i]] == 'PHASE 8':
                        print(name_of_players[i] + ' has completed the Phase 7!')
                        cards.clear()
                        draw_pile.clear()
                        for i in range(0, number_of_players):
                            del players_cards[name_of_players[i]]
                        set_cards()
                        shuffle_and_deal()   
                elif all_phases[name_of_players[i]] == 'PHASE 8':
                    all_phases[name_of_players[i]] = phase8.phase_eight(players_cards, name_of_players[i])
                   #Setting dictionary vlue for player to new phase
                    if all_phases[name_of_players[i]] == 'PHASE 8':
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]]
                    else:
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]][0]
                   #slicing list to only get the card values that follow the phase at index 0
                    new_list = all_phases[name_of_players[i]][1:]
                    print(all_phases)
                    if all_phases[name_of_players[i]] == 'PHASE 9':
                        print(name_of_players[i] + ' has completed the Phase 8!')
                        cards.clear()
                        draw_pile.clear()
                        for i in range(0, number_of_players):
                            del players_cards[name_of_players[i]]
                        set_cards()
                        shuffle_and_deal()   
                elif all_phases[name_of_players[i]] == 'PHASE 9':
                    all_phases[name_of_players[i]] = phase9.phase_nine(players_cards, name_of_players[i])
                   #Setting dictionary vlue for player to new phase
                    if all_phases[name_of_players[i]] == 'PHASE 9':
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]]
                    else:
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]][0]
                   #slicing list to only get the card values that follow the phase at index 0
                    new_list = all_phases[name_of_players[i]][1:]
                    print(all_phases)
                    if all_phases[name_of_players[i]] == 'PHASE 10':
                        print(name_of_players[i] + ' has completed the Phase 9!')
                        cards.clear()
                        draw_pile.clear()
                        for i in range(0, number_of_players):
                            del players_cards[name_of_players[i]]
                        set_cards()
                        shuffle_and_deal()    
                elif all_phases[name_of_players[i]] == 'PHASE 10':
                    all_phases[name_of_players[i]] = phase10.phase_ten(players_cards, name_of_players[i])
                   #Setting dictionary vlue for player to new phase
                    if all_phases[name_of_players[i]] == 'WINNER':
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]]
                    else:
                        all_phases[name_of_players[i]] = all_phases[name_of_players[i]][0]
                   #slicing list to only get the card values that follow the phase at index 0
                    new_list = all_phases[name_of_players[i]][1:]
                    print(all_phases)
                    if all_phases[name_of_players[i]] == 'WINNER':
                        print(name_of_players[i] + ' has completed all 10 phases!')
                        cards.clear()
                        draw_pile.clear()
                        for i in range(0, number_of_players):
                            del players_cards[name_of_players[i]]
                        game_over = True  
                        
            elif choice.upper() == "END":
                game_over = True
            else:
                game_over = True
                print("Hit else statement line 119")
def main():
    set_cards()
    shuffle_and_deal()
    print(draw_pile)
    next_round()
    next_game = input(print("Game over. Do you want to play again? "))
    if next_game.upper() == "YES":
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()


    