# Задача 2. Игроки
# Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет, а также его текущий статус,
# в котором указано, отдыхает он, тренируется или путешествует:
#
# Напишите программу, которая выводит на экран вот такие данные в разных строчках:
#
# 1. Все члены команды из команды А, которые отдыхают.
# 2. Все члены команды из группы B, которые тренируются.
# 3. Все члены команды из команды C, которые путешествуют.

players_dict = {

    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}

}

team_a_players = [

    player["name"]
    for player in players_dict.values()
    if player["team"] == "A" and player["status"] == "Rest"

]
print(f"\n{', '.join(team_a_players)}")


team_b_players = [

    player["name"]
    for player in players_dict.values()
    if player["team"] == "B" and player["status"] == "Training"

]
print(f"\n{', '.join(team_b_players)}")


team_c_players = [

    player["name"]
    for player in players_dict.values()
    if player["team"] == "C" and player["status"] == "Travel"

]
print(f"\n{', '.join(team_c_players)}")