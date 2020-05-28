
 #Crescimento da população brasileira 1980 - 2016
 #Fonte = DataSus
import matplotlib.pyplot as plt #importa a biblioteca responsável pela visualização de gráficos

dados = open("original.csv").readlines()

x = [] #Anos
y = [] #População

###o bloco seguinte pega os valores de x e y da tabela e separa em dois vetores
for i in range(len(dados)):
	if i != 0:
		linha = dados[i].split(";")
		x.append(int(linha[0]))
		y.append(int(linha[1]))

plt.bar(x, y, color="#e4e4e4") #plota o grafico em barras, com atributos modificados (cor)
plt.plot(x, y, color = "k", linestyle = "--") #plota o grafico em linha, com atributos modificados (cor e estilo da linha)

plt.title("Crescimento da população brasileira 1980 - 2016") #Título do grafico
plt.xlabel("Ano") #legenda do eixo x
plt.ylabel("População x100.000.000") #legenda do eixo y
#plt.show() #mostra o gráfico plotado
plt.savefig("populacao_brasileira.pdf")
