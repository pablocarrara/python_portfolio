#Supongamos que queremos contar los puntos convertidos por los mosquitos de obrero en 2 torneos diferentes

from collections import Counter


basketball_players = [
    {'name': 'Joa', 'points': 250, 'tournament': 'Student day'},
    {'name': 'Ale', 'points': 300, 'tournament': 'Student day'},
    {'name': 'Augusto', 'points': 400, 'tournament': 'Student day'},
    {'name': 'Bauti', 'points': 200, 'tournament': 'Student day'},
    {'name': 'Iker', 'points': 180, 'tournament': 'Student day'},
    {'name': 'Joa', 'points': 100, 'tournament': 'Spring week'},
    {'name': 'Ale', 'points': 350, 'tournament': 'Spring week'},
    {'name': 'Augusto', 'points': 380, 'tournament': 'Spring week'},
    {'name': 'Bauti', 'points': 280, 'tournament': 'Spring week'},
    {'name': 'Iker', 'points': 320, 'tournament': 'Spring week'}
]



results = Counter()


for player in basketball_players:
    results[player['name']] += player['points']


print(dict(results))

# lo mismo pero de una forma mas clasica, sin usar el Counter()

results = {}



# Contando los puntos de cada jugador dentro del diccionario results

for player in basketball_players:
    if player['name'] in results:
        results[player['name']] += player['points']
    else:
        results[player['name']] = player['points']



# Imprimo el dicionario que cuenta los puntos de cada jugador

print(results)


