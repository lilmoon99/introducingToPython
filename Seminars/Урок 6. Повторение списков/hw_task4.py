# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков

# Конкретный пример ввода-вывода приведён ниже.

# Порядок вывода команд произвольный.

# Пример входа:

# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# Выход будет:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
from random import *
teams = ["Зенит", "ЦСКА", "Спартак М", "Ростов", "Ахмат", "Краснодар", "Оренбург", "Локомотив М", "Динамо М", "Сочи", "Урал", "Крылья Советов", "Пари Нижний Новгород", "Факел", "Химки", "Торпедо М"]
championship = {"Зенит":[], "ЦСКА":[], "Спартак М":[], "Ростов":[], "Ахмат":[], "Краснодар":[], "Оренбург":[], "Локомотив М":[], "Динамо М":[], "Сочи":[], "Урал":[], "Крылья Советов":[], "Пари Нижний Новгород":[], "Факел":[], "Химки":[], "Торпедо М":[]}
matches_played_count = {"Зенит":0, "ЦСКА":0, "Спартак М":0, "Ростов":0, "Ахмат":0, "Краснодар":0, "Оренбург":0, "Локомотив М":0, "Динамо М":0, "Сочи":0, "Урал":0, "Крылья Советов":0, "Пари Нижний Новгород":0, "Факел":0, "Химки":0, "Торпедо М":0}
points = {"win": 3,
          "draw" : 1,
          "lose" : 0}

def init_match():
    team1 = choice(teams)
    team2 = choice(teams)
    while(team1 == team2):
        team2 = choice(teams)
    print(f"Сегодня играют {team1} против {team2}.")
    team1_score = int(input(f"Количество голов у {team1}: "))
    team2_score = int(input(f"Количество голов у {team2}: "))
    if team1_score > team2_score:
        if team1_score > 5:
            print(f"{team1} поиздевались над {team2}")
        print(f"{team1} выиграл.")
        championship[team1].append(points["win"])
        championship[team2].append(points["lose"])
        
    elif team1_score < team2_score:
        if team2_score > 5:
            print(f"{team2} поиздевались над {team1}")
        print(f"{team2} выиграл.")
        championship[team2].append(points["win"])
        championship[team1].append(points["lose"])
    else:
        print(f"Ничья между {team1} и {team2}.")
        championship[team1].append(points["draw"])
        championship[team2].append(points["draw"])
    matches_played_count[team1] = matches_played_count[team1] + 1
    matches_played_count[team2] = matches_played_count[team2] + 1
        


def play_games(match_count):
    for i in range(match_count):
        init_match()

def print_table(champ_dict,played_matches_dict):
    for i in teams:
        if played_matches_dict[i] == 0:
            played_matches_dict.pop(i)
            
    for i in teams:
        if i in played_matches_dict:
            print(f"{i}. Матчей сыграно: {played_matches_dict[i]}. Очки: {champ_dict[i]}. Итого: {sum(champ_dict[i])}")
    
    
matches_played = int(input("Введите количество сыгранных матчей: "))
play_games(matches_played)
# print(championship)
# print(matches_played_count)
print_table(championship,matches_played_count)