import random

def roll():
    return random.randrange (1, 7)

numbers = []

for i in range(0, 100):
    numbers.append(roll())

qtd1 = qtd2 = qtd3 = qtd4 = qtd5 = qtd6 = 0

for n in numbers:
    if n == 1:
        qtd1 += 1
    elif n == 2:
        qtd2 += 1
    elif n == 3:
        qtd3 += 1
    elif n == 4:
        qtd4 += 1
    elif n == 5:
        qtd5 += 1
    elif n == 6:
        qtd6 += 1

print(numbers)
print('Quantidade que cada valor foi conseguido no dado:\n')
print('1: {} vezes \n2: {} vezes \n3: {} vezes \n4: {} vezes \n5: {} vezes \n6: {} vezes'.format(qtd1, qtd2, qtd3, qtd4, qtd5, qtd6))