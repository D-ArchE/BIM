def calcular_bim():
    largura = float(input("Digite a largura do bloco em cm: "))
    altura = float(input("Digite a altura do bloco em cm: "))
    comprimento = float(input("Digite o comprimento do bloco em cm: "))
    altura_coluna = float(input("Digite a altura da coluna em metros: "))
    distancia_entre_colunas = float(input("Digite a distância entre as colunas em metros: "))

    # Converter medidas para metros
    largura = largura / 100
    altura = altura / 100
    comprimento = comprimento / 100

    # Calcular a quantidade de blocos por coluna
    altura_coluna_cm = altura_coluna * 100
    qtd_blocos_coluna = altura_coluna_cm // altura

    # Calcular a quantidade de colunas necessárias para uma parede com 2m de distância entre as colunas
    distancia_entre_colunas_cm = distancia_entre_colunas * 100
    largura_parede_cm = largura * 100
    qtd_colunas = largura_parede_cm // (largura + distancia_entre_colunas_cm)
    if largura_parede_cm % (largura + distancia_entre_colunas_cm) != 0:
        qtd_colunas += 1

    # Calcular a quantidade total de blocos
    qtd_blocos_total = qtd_colunas * qtd_blocos_coluna + (largura_parede_cm - distancia_entre_colunas_cm * (qtd_colunas - 1)) * altura_coluna_cm // altura

    # Imprimir os resultados
    print(f"Quantidade de blocos por coluna: {qtd_blocos_coluna:.0f}")
    print(f"Quantidade de colunas necessárias: {qtd_colunas:.0f}")
    print(f"Quantidade total de blocos (incluindo os de coluna): {qtd_blocos_total:.0f}")
    print(f"Quantidade total de blocos (sem os de coluna): {(largura_parede_cm * altura_coluna_cm // altura):.0f}")

calcular_bim()
