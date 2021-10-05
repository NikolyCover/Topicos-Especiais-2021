import sys

def media(numbers):
    sum = 0

    for number in numbers:
        sum += number
    
    media = sum / len(numbers)
    return media

if sys.version_info.major == 2:
    name = raw_input('Atleta: ')
elif sys.version_info.major == 3:
    name = input('Atleta: ')

jumps = []
jumps.append(input('\nPrimeiro Salto: '))
jumps.append(input('Segundo Salto: '))
jumps.append(input('Terceiro Salto: '))
jumps.append(input('Quarto Salto: '))
jumps.append(input('Quinto Salto: '))

print('\nResultado final:')
print('Atleta: ' + name)
print('Saltos: {} - {} - {} - {} - {}'.format(jumps[0], jumps[1], jumps[2], jumps[3], jumps[4]))
print('{} m'.format(media(jumps)))
