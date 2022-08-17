with open('arquivo.txt', 'r') as arquivo:
    mensagem = arquivo.readlines()
lista = [x.strip('\n').strip(' ') for x in mensagem]
#print(lista)

for linha in range(1, len(lista), 3):
    lista[linha] = lista[linha].strip()  # NOTA 01

    if lista[linha] == "U":
        n = []
        n.append(lista[linha + 1])
        n.append(lista[linha + 2])
        print(f'União: conjunto 1: {lista[linha + 1]} conjunto 2: {lista[linha + 2]} Resultado: {n}')
    #Inter
    elif lista[linha] == "I":
        p = []
        o = []
        p.append(lista[linha + 1])
        o.append(lista[linha + 2])
        print(f'Interseção: conjunto 1 {p},conjunto 2 {o} Resultado {p and o}')
    #Diferença
    elif lista[linha] == "D":
        diferenca = []
        conjunto_1 = lista[linha + 1]
        conjunto_2 = lista[linha + 2]
        for valor in conjunto_1:
            if valor not in conjunto_2:
                diferenca.append(valor)
        for valor in conjunto_2:
            if valor not in conjunto_1 and valor not in diferenca:
                diferenca.append(valor)
        print(f'diferença: conjunto 1 [{conjunto_1}], conjunto 2 [{conjunto_2}] Resultado: {diferenca}')

    #Cartb
    elif lista[linha] == "C":
        x = lista[linha + 1].split(', ')
        y = lista[linha + 2].split(', ')
        cart = []

        for i in y:
            for k in x:
                cart.append([f"{k}, {i}"])

        print(f'cartesiano: conjunto 1 {x} conjunto 2 {y} Resultado: {cart}')