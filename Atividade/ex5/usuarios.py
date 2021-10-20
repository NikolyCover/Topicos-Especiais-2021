import pandas as pd

def byteToMegabyte(num):
    return num / 1048576

def percent(num, total):
    return round(((num / total) * 100), 2)

def media(total, qtd):
    return total / qtd

def totalOf(list):
    total = 0

    for iten in list:
        total += iten

    return total

with open("C:\Users\Nikoly\Documents\Produtividade\IFPR\IFPR2021\TopicosEspeciais\Python\Atividade\ex5\users.txt", "r") as archive:
    content = archive.readlines()

usuarios = []
values = []

i = 1
total = 0

for line in content:
    armazenamento = byteToMegabyte(float(line.split(' ')[1].replace('\n', '')))
    values.append(armazenamento)

    usuarios.append({
        'Nr.' : i,
        'Usuario' : line.split(' ')[0],
        'Espaco utilizado' : str(round(armazenamento, 2)) + ' MB',
    })
    i += 1

i = 0
for user in usuarios:
    user['% do uso'] = str(percent(values[i], totalOf(values))) + ' %'
    i += 1

usuarios_df = pd.DataFrame(usuarios)

with open('relatorio.txt', 'w') as relatorio:
    relatorio.write('ACME Inc.           Uso do espaco em disco pelos usuarios\n---------------------------------------------------------\n')
    relatorio.write(usuarios_df.to_string(index=False, col_space=5, justify='left'))
    relatorio.write('\n\nEspaco total ocupado: {} MB'.format(round(totalOf(values), 2)))
    relatorio.write('\nEspaco medio ocupado: {} MB'.format(round(media(totalOf(values), len(usuarios)), 2)))
