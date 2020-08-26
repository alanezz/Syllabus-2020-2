import random
import csv

dates = range(1, 6)

data = []
for i in dates:
    scored = set()
    for j in range(20):
        scored.add(random.randint(1,30))
    for player in scored:
        goals = random.randint(1,4)
        t = (f'Jugador {player}', i, goals)
        data.append(t)

random.shuffle(data)

data_file = open('data.csv', 'w', encoding='utf-8')
writer = csv.writer(data_file)

for row in data:
    writer.writerow(row)

data_file.close()