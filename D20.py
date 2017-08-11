import random
print('Bilando o dado...')
for i in range(1):
    roll = random.randint(1, 20)
    print(roll)
if roll == 20:
    print('Eu quero que você se foda e que meu pau cresça! Rolada crítica!')
    exit()
if roll == 1:
    print('Você broxou! Falha Crítica!')
    exit()
    print('Quer tentar de novo?')