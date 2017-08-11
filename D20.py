import random
print('Rolando o dado...')
for i in range(1):
    roll = random.randint(1, 20)
    print(roll)
if roll == 20:
    print('Rolada crítica!')
    exit()
if roll == 1:
    print('Falha Crítica!')
    exit()
    print('Quer tentar de novo?')
