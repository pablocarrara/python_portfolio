# Crear un diccionario con los nombres de los jugadores y sus puntos
nba_players = {
    "LeBron James": 30,
    "Anthony Davis": 25,
    "Russell Westbrook": 20,
    "Carmelo Anthony": 15,
    "Dwight Howard": 12,
    "Malik Monk": 18,
    "Trevor Ariza": 10,
    "Wayne Ellington": 14
}

# Encontrar al jugador con la mayor cantidad de puntos
key_max = max(nba_players.keys(), key=lambda k: nba_players[k])

# Encontrar al jugador con la menor cantidad de puntos
key_min = min(nba_players.keys(), key=lambda k: nba_players[k])

# Imprimir los resultados
print(f'La mayor cantidad de puntos le corresponde a {key_max} quien convirtió {nba_players[key_max]} puntos.')
print(f'La menor cantidad de puntos le corresponde a {key_min} quien convirtió {nba_players[key_min]} puntos.')
