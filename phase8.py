def phase_eight(current_player, key):
    print("Phase Eight is 7 cards of a color")
    seven_of_one_color = []
    number_ending = ""
    for i in range(1,8):
        if i == 1:
            number_ending = "1st"
        elif i == 2:
            number_ending = "2nd"
        elif i == 3:
            number_ending = "3rd"
        elif i == 4:
            number_ending = "4th"
        elif i == 5:
            number_ending = "5th"
        elif i == 6:
            number_ending = "6th"
        elif i == 7:
            number_ending = "7th"
        seven_of_one_color_input = input("What is the {card} card of your 7 cards of one color? ".format(card=number_ending))
        if seven_of_one_color_input.upper() not in current_player.get(key):
            input("What is the {card} card of your 7 cards of one color? ".format(card=number_ending))       
        seven_of_one_color_input = seven_of_one_color_input.upper()
        seven_of_one_color.append(seven_of_one_color_input)
    phase = seven_of_one_color
    print(phase)
    check_sets = all(elem in current_player.get(key) for elem in phase)
    numbers = []
    for i in range(len(phase)):
        if phase[i] == 'WILD':
            check = phase[i]
            numbers.append(check.strip())
        else:
            check = phase[i][2:]
            numbers.append(check.strip())            
    print(numbers)

    #Set check_numbers to false as default
    check_numbers = False
    #check that the numbers in the set are equal or WILD
    if (numbers[0] == numbers [1] or numbers[0] == 'WILD' or numbers [1] == 'WILD') \
    and (numbers[1] == numbers[2] or numbers[1] == 'WILD' or numbers [2] == 'WILD') \
    and (numbers[2] == numbers[3] or numbers[2] == 'WILD'or numbers [3] == 'WILD') \
    and (numbers[4] == numbers[5] or numbers[4] == 'WILD' or numbers [5] == 'WILD') \
    and (numbers[5] == numbers[6] or numbers[5] == 'WILD' or numbers [6] == 'WILD') \
    and (numbers[6] == numbers[7] or numbers[6] == 'WILD' or numbers [7] == 'WILD'):
        check_numbers = True
    else:
        check_numbers = False
    if check_sets == True and check_numbers == True:
        #remove played cards from players hand.
        remaining_cards = current_player.get(key)
        for card in phase:
            print(card)
            if card in remaining_cards:
                remaining_cards.remove(card)  
                print(remaining_cards) 
        print(remaining_cards) 
        outcome = ['PHASE 9'] 
        for card in remaining_cards:
            outcome.append(card)
        print(outcome)
    else:
        outcome = "PHASE 8"
    return outcome

