# Função para calcular a quantidade de colunas necessárias
def calcular_quantidade_colunas(distancia_entre_colunas_m, distancia_minima_m):
    quantidade_colunas = 1
    distancia_atual_m = distancia_entre_colunas_m
    
    while distancia_atual_m > distancia_minima_m:
        quantidade_colunas += 1
        distancia_atual_m = distancia_entre_colunas_m / quantidade_colunas
    
    return quantidade_colunas

# Solicita informações ao usuário
largura_bloco_cm = float(input("Informe a largura do bloco de construção em centímetros: "))
altura_bloco_cm = float(input("Informe a altura do bloco de construção em centímetros: "))
comprimento_bloco_cm = float(input("Informe o comprimento do bloco de construção em centímetros: "))
altura_coluna_m = float(input("Informe a altura da coluna em metros: "))
distancia_entre_colunas_m = float(input("Informe a distância entre as colunas em metros: "))

# Calcula quantidade de blocos na altura da coluna
altura_bloco_m = altura_bloco_cm / 100
quantidade_blocos_coluna = round(altura_coluna_m / altura_bloco_m)

# Calcula quantidade de colunas para a largura informada
largura_bloco_m = largura_bloco_cm / 100
comprimento_bloco_m = comprimento_bloco_cm / 100
distancia_entre_colunas_cm = distancia_entre_colunas_m * 100
quantidade_colunas = round(distancia_entre_colunas_cm / comprimento_bloco_m)

# Calcula quantidade de blocos para a parede
quantidade_blocos_parede = quantidade_colunas * quantidade_blocos_coluna

# Imprime resultado
print(f"A quantidade total de blocos necessários para construir a parede é de {quantidade_blocos_parede} blocos.")

# Calcula quantidade de colunas necessárias com distância mínima de 2 metros
distancia_minima_m = 2
quantidade_colunas_distancia_minima = calcular_quantidade_colunas(distancia_entre_colunas_m, distancia_minima_m)

# Imprime resultado
print(f"Para que a parede fique forte, é necessário utilizar {quantidade_colunas_distancia_minima} colunas a cada 2 metros.")
