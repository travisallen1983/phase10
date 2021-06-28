def phase_seven(current_player, key):
    print("Phase Seven is two sets of four")
    set_of_four_one = []
    set_of_four_two = []
    number_ending = ""
    for i in range(1,5):
        if i == 1:
            number_ending = "1st"
        elif i == 2:
            number_ending = "2nd"
        elif i == 3:
            number_ending = "3rd"
        elif i == 4:
            number_ending = "4th"
        set_of_four_one_input = input("What is the {card} card of your first set of 4? ".format(card=number_ending))
        if set_of_four_one_input.upper() not in current_player.get(key):
            input("What is the {card} card of your first set of 4? ".format(card=number_ending))
        set_of_four_one_input = set_of_four_one_input.upper()
        set_of_four_one.append(set_of_four_one_input)
    for i in range(1,5):
        if i == 1:
            number_ending = "1st"
        elif i == 2:
            number_ending = "2nd"
        elif i == 3:
            number_ending = "3rd"
        elif i == 4:
            number_ending = "4th"
        set_of_four_two_input = input("What is {card} card of your second set of 4? ".format(card=number_ending))
        if set_of_four_two_input.upper() not in current_player.get(key):
            input("What is the {card} card of your second set of 4? ".format(card=number_ending))
        set_of_four_two_input = set_of_four_two_input.upper()
        set_of_four_two.append(set_of_four_two_input)
    phase = set_of_four_one + set_of_four_two
    print(phase)
    check_sets = all(elem in current_player.get(key) for elem in phase)
    numbers_raw = []
    numbers = []
    for i in range(len(phase)):
        check = phase[i][:2]
        numbers_raw.append(check.strip())
    print(numbers_raw)
    for number in numbers_raw:
        if number == "WI":
           numbers.append(-1)
        else:
            numbers.append(int(number))
    print(numbers)
    #Set check_numbers to false as default
    check_numbers = False
    #check that the numbers in the set are equal or WILD
    if (numbers[0] == numbers [1] or numbers[0] == -1 or numbers [1] == -1) \
    and (numbers[1] == numbers[2] or numbers[1] == -1 or numbers [2] == -1) \
    and (numbers[2] == numbers[3] or numbers[2] == -1 or numbers [3] == -1) \
    and (numbers[4] == numbers[5] or numbers[4] == -1 or numbers [5] == -1) \
    and (numbers[5] == numbers[6] or numbers[5] == -1 or numbers [6] == -1) \
    and (numbers[6] == numbers[7] or numbers[6] == -1 or numbers [7] == -1):
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
        outcome = ['PHASE 8'] 
        for card in remaining_cards:
            outcome.append(card)
        print(outcome)
    else:
        outcome = "PHASE 7"
    return outcome

