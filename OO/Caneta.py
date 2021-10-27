class Caneta:
    
    cor = ''
    modelo = ''
    carga = ''
    tampada = ''

    def __init__(self, cor, modelo) -> None:
        pass

bicAzul = Caneta()
bicAzul.cor = 'azul'
bicAzul.modelo = 'esferográfica'
bicAzul.carga = '50%'
bicAzul.tampada = True
print(bicAzul.cor)