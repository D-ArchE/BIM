def calc_bim():
    largura = float(input("Digite a largura do bloco (em centímetros): "))
    altura = float(input("Digite a altura do bloco (em centímetros): "))
    comprimento = float(input("Digite o comprimento do bloco (em centímetros): "))
    altura_coluna = float(input("Digite a altura da coluna (em metros): "))
    espaco_largura = float(input("Digite o espaço entre cada bloco na largura (em centímetros): "))
    espaco_altura = float(input("Digite o espaço entre cada bloco na altura (em centímetros): "))
    distancia_colunas = float(input("Digite a distância entre uma coluna e outra (em metros): "))

    largura_cm = largura + espaco_largura
    altura_cm = altura + espaco_altura

    altura_coluna_cm = altura_coluna * 100
    distancia_colunas_cm = distancia_colunas * 100

    quantidade_colunas = int(altura_coluna_cm // altura_cm)
    quantidade_blocos_coluna = int((altura_coluna_cm - espaco_altura) // altura_cm)

    quantidade_blocos_largura = int((43.47 * 100) // largura_cm)

    quantidade_total_blocos = quantidade_blocos_coluna * quantidade_blocos_largura * quantidade_colunas

    quantidade_total_bloco_sem_coluna = (quantidade_blocos_coluna * (quantidade_blocos_largura - 1) + 2) * quantidade_colunas

    espaco_cimento_largura = (quantidade_blocos_largura - 1) * (altura_cm / 100) * (43.47 / 100)
    espaco_cimento_altura = quantidade_colunas * (distancia_colunas_cm / 100) * (largura_cm / 100)

    quantidade_furos_bloco = int(input("Digite a quantidade de furos/legos do bloco: "))
    quantidade_ferro_furo = int(input("Digite a quantidade de ferros que vão em cada furo/lego do bloco: "))

    quantidade_total_ferro_coluna = quantidade_blocos_coluna * quantidade_furos_bloco * quantidade_ferro_furo
    quantidade_total_ferro_parede = (quantidade_colunas - 1) * (quantidade_blocos_largura * quantidade_furos_bloco) * quantidade_ferro_furo

    print("Quantidade total de blocos:", quantidade_total_blocos)
    print("Quantidade de blocos por coluna:", quantidade_blocos_coluna)
    print("Quantidade de blocos por espaço de parede:", quantidade_blocos_largura - 1)
    print("Quantidade total de blocos sem contar as colunas:", quantidade_total_bloco_sem_coluna)

    print("Quantidade de massa de cimento necessária para preencher os espaços entre os blocos na largura: %.2f metros cúbicos" % espaco_cimento_largura)
    print("Quantidade de massa de cimento necessária para preencher os espaços entre os blocos na altura: %.2f metros cúbicos" % espaco_cimento_altura)

    print("Quantidade total de ferro de construção por coluna:", quantidade_total_ferro_coluna)
    print("Quantidade total de ferro de construção por espaço de parede:", quantidade_total_ferro_parede)

calc_bim()
