import random

for i in range(3):
    print(random.random())

for i in range(5):
    print(random.randint(1, 20))
    

teams = ['Juventus', 'Barcelona', 'Real Madrid', 'Bayern Munich', 'Manchester City', 'Paris Saint Germain', 'Chelsea', 'AC Milan']
winner = random.choice(teams)
print(winner)