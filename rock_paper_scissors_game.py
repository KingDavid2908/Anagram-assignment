from random import choice

def rock_paper_scissors():
    #person input
    print('Type R for rock')
    print('Type P for paper')
    print('Type S for scissors')
    player_string = input('Input a letter: ')
    player_list = []
    for player_char in player_string:
        player_list.append(player_char)
        
    player = player_list[0].capitalize()
    if player == 'R' or player == 'P' or player == 'S':
        computer_dict = {'R' : 'rock', 'P' : 'paper', 'S' : 'scissors'}
        computer_dict_keys = []
        for key, value in computer_dict.items():
            computer_dict_keys.append(key)
        computer = choice(computer_dict_keys)
        player_choice = computer_dict[player].capitalize()
        computer_choice = computer_dict[computer].capitalize()
        print('Player ({}) : CPU ({})'.format(player_choice, computer_choice))
        rock, paper, scissors = computer_dict['R'].capitalize(), computer_dict['P'].capitalize(), computer_dict['S'].capitalize()
        
        if computer_choice == player_choice:
            print('The game was tied, rechoose again')
            rock_paper_scissors()
        elif (computer_choice == rock and player_choice == paper) or (computer_choice == paper and player_choice == scissors) or (computer_choice == scissors and player_choice == rock):
            print('Player wins')
        elif (player_choice == rock and computer_choice == paper) or (player_choice == paper and computer_choice == scissors) or (player_choice == scissors and computer_choice == rock):
            print('Computer wins')

        loop = input('Do you want to continue? (yes or no) : ').lower()
        if loop == 'yes':
            rock_paper_scissors()
        else:
             print('Nice game. Thanks for playing with us')

    else:
        print('Wrong input')
        rock_paper_scissors()


print(rock_paper_scissors())
