# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
#   чтобы забрать все конфеты у своего конкурента?
# Первому игроку  нужно брать столько конфет, чтобы в сумме
#  со вторым  получалось 28. В первый ход нужно взять 20 конфет, это остаток от 2021%29
# 1 игрок | 2 игрок
# 20      | 15      = 13+15=28
# 14      | 16      = 13+16=28
# 12
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import *
import os
 
welcome = ('На столе лежит 2021 конфета.\n'
                'Играют два игрока делая ход друг после друга.\n'
                'Первый ход определяется жеребьёвкой. За один ход \n'
                'можно забрать не более чем 28 конфет.Все конфеты \n'
                'оппонента достаются сделавшему последний ход.')
print(welcome)

message = ('Твоя очередь дружок, ходи,', 'Давай, не тяни резину, ')


def player_vs_player():
    candi = 2021
    max_candi = 28
    count = 0
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = input('\nКак зовут твоего соперника?: ')

    print('\nОпеределим кто первый начнет игру.\n')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = playe
    else:
        lucky = player_2
        loser = player_1
    print(f'Поздравляю {lucky}, ты ходишь первым !') 

    while candi > 0:
        if count == 0:
            step = int (input(f'\n{choice(message)} {lucky} = '))
            if step == 0 or step > max_candi:
                step = int (input(f'\nМожно взять только {max_candi} конфет, попробуй еще раз: '))
            candi = candi - step
        if candi > 0:
            print (f'\nНе расслабляйтесь, еще {candi} конфет')
            count =1 
        else:
            print ('Ммм, закончились сладости')
        
        if count == 1:
            step = int(input(f'\n{choice(message)} {loser} = '))
            if step == 0 or step > max_candi:
                step = int(input(f'\nМожно взять только {max_candi} конфет, не будь жадиной, поgробуй еще раз: '))
            candi = candi - step
        if candi > 0:
            print (f'\nНе расслабляйтесь, еще {candi} конфет')
            count = 0 
        else:
            print ('Ммм, закончились слодости')
        
    if count == 1:
        print(f'{loser} ПОБЕДИЛ')
    if count == 0:
        print(f'{lucky} ПОБЕДИЛ')

player_vs_player()


def player_vs_bot():
    candi= 2021
    max_candi = 28
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    print(f'\nНу что же {player_1} и  {player_2} да начнется игра !\n')
    print('\nДля начала опеределим кто начнет игру.\n')

    lucky = randint(-1, 0)

    print(f'Поздравляю {players[lucky+1]} ты ходишь первым !')

    while candi> 0:
        lucky += 1
        if players[lucky % 2] == 'Компьютер':
            print(f'\nХодит {players[lucky%2]} \nНа кону {candi}. \n{choice(message)}: ')
            if candi< 29:
                step = candi
            else:
                ostatok = ((candi//28)*max_candi)+1
                step = candi - ostatok
                if step == -1:
                    step = max_candi -1
                if step == 0:
                    step = max_candi
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nНу ходи,  {players[lucky%2]} \nНа кону {candi} {choice(message)}:  '))
            while step > max_candi or step > candi:
                step = int(input(f'\nЗа один ход можно взять {max_candi} конфет, попробуй еще раз: '))
        candi= candi- step

    print(f'На кону осталось {candi} \nПобедил {players[lucky%2]}')

player_vs_bot()