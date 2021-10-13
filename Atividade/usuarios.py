import pandas as pd

def byteToMegabyte(num):
    return num / 1000000

def percent(num, total):
    # x% * total = part
    # x% = part / total
    return round(((num / total) * 100), 2)

def sum(dict, key):
    return 0

with open("usuarios.txt", "r") as archive:
    content = archive.readlines()

usuarios = []

i = 1
total = 0

for line in content:
    armazenamento = byteToMegabyte(float(line.split(' ')[1].replace('\n', '')))
    total += armazenamento

    usuarios.append({
        'Nr.' : i,
        'usuario' : line.split(' ')[0],
        'armazenamento' : str(round(armazenamento, 2)) + ' MB',
    })
    i += 1

usuarios_df = pd.DataFrame(usuarios)
print(usuarios)

with open('relatorio.txt', 'w') as relatorio:
    relatorio.write('ACME Inc.           Uso do espaco em disco pelos usuarios\n---------------------------------------------------------\n')
    relatorio.write(usuarios_df.to_string(index=False, col_space=5, justify='left'))
    relatorio.write('\n\nEspaco total ocupado: ')
    relatorio.write('\nEspaco medio ocupado: ')
