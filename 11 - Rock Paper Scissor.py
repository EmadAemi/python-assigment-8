from random import randint

choices = ['Rock', 'Scissors', 'Paper']
scores = {'PC': 0, 'Player': 0}

for i in range(10):
    while True:
        p1 = int(input("1 for Rock, 2 for Paper, 3 for Scissor: ")) - 1
        if p1 in [0, 1, 2]: break
    p2 = randint(0, 2)
    print(choices[p2])
    if p1 == p2: pass
    elif p2 % 3 == (p1 + 1) % 3: scores['PC'] += 1
    else: scores['Player'] += 1
print('Player:', scores['Player'], '\nPC:', scores['PC'])
