
print("Digite separado por espaço, o dia, produto, qtd, e preço  \n")

arq = open('C:\\vendas_diarias.txt', 'w')

for n in range(2):
    x = input()
    arq.write(x + "\n")

arq.close()

arq = open('C:\\vendas_diarias.txt', 'r')

prod = []
prodT = []
prod2 = []
while True :
    s = arq.readline()
    if s == "": break
    x = s.split(" ")
    prod.append(x[1])

prod2 = sorted(set(prod))

qtdV = 0
qtdD = 0
arq.close()

arq2 = open('C:\\vendas_diarias.txt', 'r')
for n in range(len(prod2)):
    for p in range(len(prod)):
        q = arq2.readline()
        if q == "": break
        z = q.split(" ")
        if (prod2[n] == prod[p]):
            qtdV = qtdV + int(z[2])
            qtdD = qtdD + int(z[3])

    prodT.append(prod2[n] + " " + str(qtdV) + " " + str(qtdD))
    qtdV = 0
    qtdD = 0
    arq2.seek(0)

arq2.close()
arq3 = open('C:\\totais_produtos.txt', 'w')

for d in range(len(prod2)):
    arq3.write(prodT[d] + "\n")

arq3.close()