'''
剪刀石头布游戏
计算机将是你的对手，可以像你一样，为每一步随机选择一个元素（rock、paper 或 scissors）。
玩家可以选择三个选项之一（rock、paper 或 scissors），如果玩家输入了无效选项，应向其发出警告。
在每一轮，玩家必须输入列表中的一个选项，并会收到他们是赢了、输了还是与对手打平的通知。
在每个回合结束时，玩家可以选择是否再玩一次。
游戏结束时显示玩家的分数。
小游戏必须处理用户输入，将其变为小写，并在选项无效时通知用户。
'''

import random

def game():
    # 定义一个列表
    options = ['rock', 'paper', 'scissors']
    # 定义一个字典
    results = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    # 定义一个变量
    player_score = 0
    # 定义一个变量
    computer_score = 0
    # 定义一个变量
    play = True
    # 定义一个变量
    round = 1
    # 定义一个变量
    player_choice = ''
    # 定义一个变量
    computer_choice = ''
    # 定义一个变量
    result = ''
    # 定义一个变量
    play_again = ''
    # 定义一个变量
    valid = False

    while play:
        print(f'Round {round}')
        while not valid:
            player_choice = input('rock, paper or scissors? ').lower()
            if player_choice in options:
                valid = True
            else:
                print('Invalid option. Please try again.')
        computer_choice = random.choice(options)
        if results[player_choice] == computer_choice:
            player_score += 1
            result = 'win'
        elif results[computer_choice] == player_choice:
            computer_score += 1
            result = 'lose'
        else:
            result = 'draw'
        print(f'You chose {player_choice}, computer chose {computer_choice}. You {result}!')
        print(f'Score: You {player_score}, Computer {computer_score}')
        valid = False
        round += 1
        while play_again not in ['yes', 'no']:
            play_again = input('Do you want to play again? (yes/no) ').lower()
        if play_again == 'no':
            play = False
        play_again = ''
    print(f'Final score: You {player_score}, Computer {computer_score}')

if __name__ == '__main__':
    game()


    