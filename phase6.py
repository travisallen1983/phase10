def phase_six(current_player, key):
    print("Phase Six is one run of 9")
    run_of_nine = []
    number_ending = ""
    for i in range(1,10):
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
        elif i == 8:
            number_ending = "8th"
        elif i == 8:
            number_ending = "9th"
        run_of_nine_input = input("What is the {card} card of your run of 9? ".format(card=number_ending))
        if run_of_nine_input.upper() not in current_player.get(key):
            input("What is the {card} card of your run of 9? ".format(card=number_ending))
        run_of_nine_input = run_of_nine_input.upper()
        run_of_nine.append(run_of_nine_input)
    phase = run_of_nine
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
    if (numbers[0] + 1  == numbers[1] or numbers[0] == -1 or numbers [1] == -1) \
    and (numbers[1] + 1  == numbers[2] or numbers[1] == -1 or numbers [2] == -1) \
    and (numbers[2] + 1  == numbers[3] or numbers[2] == -1 or numbers [3] == -1) \
    and (numbers[3] + 1  == numbers[4] or numbers[3] == -1 or numbers [4] == -1) \
    and (numbers[4] + 1  == numbers[5] or numbers[4] == -1 or numbers [5] == -1) \
    and (numbers[5] + 1  == numbers[6] or numbers[5] == -1 or numbers [6] == -1) \
    and (numbers[6] + 1  == numbers[7] or numbers[6] == -1 or numbers [7] == -1) \
    and (numbers[7] + 1  == numbers[8] or numbers[7] == -1 or numbers [8] == -1):
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
        outcome = ['PHASE 7'] 
        for card in remaining_cards:
            outcome.append(card)
        print(outcome)
    else:
        outcome = "PHASE 6"
    return outcome


