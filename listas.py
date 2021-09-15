frutas = ['Laranja', 'Melancia', 'Pitaia', 'Pera']

frutas[1] = 'Morango'

# add um elemento ao final da lista
frutas.append('Abacate')

# add um elemento em um i especifio empurrando pra frente o que estava ali
frutas.insert(3, 'Kiwi')

# remove um elemento por um valor
frutas.remove('Laranja')

# remove o elemento do final de uma lista
frutas.pop()

for fruta in (frutas):
  print(fruta)