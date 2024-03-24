import os
import matplotlib.pyplot as plt

#Função para limpar o Terminal
def limpar_tela():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

limpar_tela()

arquivo = open('Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv', 'r')
#como o arquivo possui uma linha de cabeçalho, optei pelo método abaixo para pular a primeira linha.
next(arquivo)

#Escrita dos meses para melhor visualização ao realizar input de temperatura e corrigir dados
meses_por_extenso = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro",
}

#Dados em tuplas
dados = []

#Lê o arquivo de dados meteorológios e organiza o código em tuplas
for linha in arquivo:
    valores = linha.split(",")
    ultima = valores[4][:-1]
    tupla = ((valores[0]), float(valores[1]), float(valores[2]), float(valores[3]), float(valores[4]), float(valores[5]), float(valores[6]), float(valores[7]))
    dados.append(tupla)
arquivo.close()

#A) Função para visualizar um intervalo de dados.
def intervalo_de_dados(dados, mes_inicial, mes_final, ano_inicial, ano_final,tipo_dados):
    dados_filtrados = []
    for dado in dados:
        data = dado[0].split("/") #Segmenta a data
        ano = int(data[2])
        mes = int(data[1])

        if ano >= ano_inicial and ano <= ano_final:
            if (ano == ano_inicial and mes < mes_inicial) or (ano == ano_final and mes > mes_final):
                continue

            if tipo_dados == "todos":
                dados_filtrados.append(dado)
            elif tipo_dados == "precip":
                dados_filtrados.append((dado[0], dado[1]))
            elif tipo_dados == "temp":
                dados_filtrados.append((dado[0],dado[2], dado[3], dado[5]))
            elif tipo_dados == "umidade_vento":
                dados_filtrados.append((dado[0], dado[6], dado[7]))
                
    return dados_filtrados

#B) Função para encontrar o mês mais chuvoso.
def mes_mais_chuvoso(dados):
    meses = []
    for info in dados:
        data_completa = info[0].split("/") #Segmenta a data
        ano = data_completa[2]
        mes = data_completa[1]
        precipitacao = info[1] #segunda info é a precipitação
        data_completa = f"{mes}/{ano}"
        meses.append((data_completa, precipitacao))

    precipitacao_por_mes = {} #inicia um dicionário

    #para cada entrada de mês e precipitação, o programa armazena o mês e soma a quantidade de precipitação daquele mês.
    for mes, precipitacao in meses:
        if mes in precipitacao_por_mes:
            precipitacao_por_mes[mes] += precipitacao
        else:
            precipitacao_por_mes[mes] = precipitacao

    #O programa seleciona o mês com maior precipitação, sendo que a comparação deve ser feita com os Valores e não as chaves.
    mes_max_chuva = max(precipitacao_por_mes, key=precipitacao_por_mes.get)
    #o programa então pega o valor encontrado e seleciona a sua chave correspondente.
    max_chuva = precipitacao_por_mes[mes_max_chuva]

    return (f"{mes_max_chuva}, com {max_chuva:.2f} mm de precipitação.")

#C) Função para encontrar a média da temperatura mínima de um determinado mês
def media_temperatura_min_por_mes(dados, mes_desejado):
    media_temp_min = {}

    for info in dados:
        data_completa = info[0].split("/") #Segmenta a data
        ano_info = int(data_completa[2])
        mes_info = int(data_completa[1])
        temp_min = float(info[3]) #Converte informação de temperatura para float
        if ano_info >= 2006 and ano_info <= 2016 and mes_info == mes_desejado: #seleciona ano de 2006 até 2016
            chave = f"{mes_desejado}/{ano_info}"
            if chave in media_temp_min: #cria um dicionário com o mês e temperatura mínima
                media_temp_min[chave].append(temp_min)
            else:
                media_temp_min[chave] = [temp_min]

    for chave in media_temp_min:
        media_temp_min[chave] = sum(media_temp_min[chave]) / len(media_temp_min[chave])

    return media_temp_min

    meses_anos = list(medias_temp_min.keys())
    medias = list(medias_temp_min.values())

    plt.figure(figsize=(10, 6))
    plt.bar(meses_anos, medias, color='skyblue')
    plt.xlabel('Mês/Ano')
    plt.ylabel('Temperatura Mínima Média (°C)')
    plt.title('Média da Temperatura Mínima de um Determinado Mês nos Últimos 11 Anos')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

#D) Função para gerar gráfico
def grafico_temp_minima(media_minima,nome_mes):
    meses_anos = list(media_minima.keys())
    medias = list(media_minima.values())

    plt.figure(figsize=(6, 3))
    plt.bar(meses_anos, medias, color='skyblue')
    plt.xlabel('Mês/Ano')
    plt.ylabel('Temperatura Mínima Média (°C)')
    plt.title(f'Média da Temperatura Mínima de {nome_mes} nos Últimos 11 Anos')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

#Introdução
print(
'Olá, bem-vindo ao programa de Análise Meteorológica - Fase 2\n'
'O programa está em sua primeira fase e foi escrito por Arthur Zasso Krause\n'
'para a cadeira de Lógica e Programação de Computadores\n'
'Neste programa, será requisitado a inserção de dados meteorológicos e será feita a análise dos mesmos.\n'
)
inicio = input('Podemos iniciar? Digite "S" para sim e "N" para não: ')
if inicio.lower() == "s":
    limpar_tela()
    while True:
        print('Neste programa você terá algumas opções para acessar os dados necessários, por isso escolha a opção desejada:\n'
              "- Digite '1' para visualizar um intervalo de tempo específico dos dados meteorológicos.\n"
              "- Digite '2' para descobrir qual foi o mês mais chuvoso de todos os dados coletados.\n"
              "- Digite '3' para descobrir qual foi a média da temperatura mínima dos últimos 11 anos.\n"
              "- Digite 'Sair' para encerrar o programa.\n"
              )
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            limpar_tela()
            print('Para obter informações sobre um periodo de tempo, preciso de algumas informações.\n'
            'Lembre-se de usar 1 para Janeiro, 2 para Fevereiro, 3 para Março e assim por diante.\n'
            'O banco de dados é formado de 1967 até 2016.\n'
            )
            mes_inicial = input("Insira o mês de inicial: ")
            mes_final = input("Insira o mês de final: ")
            ano_inicial = input("Insira o ano de inicial: ")
            ano_final = input("Insira o mês de final: ")
            #Tratamento de dados: Permite apenas números entre 1 e 12 e ano entre 1967 e 2016
            while True:
                try:
                    mes_inicial = int(mes_inicial)
                    mes_final = int(mes_final)
                    ano_inicial = int(ano_inicial)
                    ano_final = int(ano_final)
                    if 1 <= mes_inicial <= 12 and 1 <= mes_final <= 12 and 1967 <= ano_inicial <= 2016 and 1967 <= ano_final <= 2016:
                        break
                    else:
                        limpar_tela()
                        print(f'você inseriu:\n'
                              f'Mês incial: {mes_inicial}\n'
                              f'Mês final: {mes_final}\n'
                              f'Ano inicial: {ano_inicial}\n'
                              f'Ano final: {ano_final}\n'
                              'Confira os valores e tente novamente.\n\n'
                            'Por favor, digite um valor entre 1 e 12 (De Janeiro a Dezembro) e um ano entre 1967 e 2016. Use apenas números.')
                        mes_inicial = input("Insira o mês de inicial: ")
                        mes_final = input("Insira o mês de final: ")  
                        ano_inicial = input("Insira o ano de inicial: ")
                        ano_final = input("Insira o mês de final: ")
                except:
                        limpar_tela()
                        print(f'você inseriu:\n'
                              f'Mês incial: {mes_inicial}\n'
                              f'Mês final: {mes_final}\n'
                              f'Ano inicial: {ano_inicial}\n'
                              f'Ano final: {ano_final}\n'
                              'Confira os valores e tente novamente.\n\n'
                            'Por favor, digite um valor entre 1 e 12 (De Janeiro a Dezembro) e um ano entre 1967 e 2016. Use apenas números.')
                        mes_inicial = input("Insira o mês de inicial: ")
                        mes_final = input("Insira o mês de final: ")
                        ano_inicial = input("Insira o ano de inicial: ")
                        ano_final = input("Insira o mês de final: ")
            # Caso o usuário insira o ano inicial maior do que o final, o pograma inverte os dados.
            if ano_inicial > ano_final:
                ano_inicial, ano_final = ano_final, ano_inicial
            limpar_tela()
            #Opção de escolha do tipo de dado que sera mostrado.
            print('Já coletei seus dados. Para o periodo informado, escolha a opção:\n'
                  '- Digite "1" para ver todos os dados\n'
                  '- Digite "2" para ver apenas os dados de precipitação\n'
                  '- Digite "3" para ver apenas os dados de temperatura\n'
                  '- Digite "4" para ver apenas os dados de umidade e vento\n')
            
            escolha_opcao_1 = input("Digite sua escolha: ")
                   
            while True:
                #Trata a escolha inserida
                try:
                    escolha_opcao_1 = int(escolha_opcao_1)
                    #Formata a função para que facilite a leitura do usuário dos dados fornecidos.
                    if 1 <= escolha_opcao_1 <= 4:
                        if escolha_opcao_1 == 1:
                        #Exibe no prompt todos os dados coletados
                            tipo_dados = "todos"
                            banco_tupla = intervalo_de_dados(dados, mes_inicial, mes_final, ano_inicial, ano_final,tipo_dados)
                            for data, precipitacao, minima, maxima, horas_insol, media, umidade, vento in banco_tupla:
                                print(f'Data: {data}, Precipitação {precipitacao}m², Temp.mínima: {minima}ºC, Temp.máxima: {maxima}ºC, Horas insolaradas: {horas_insol}h Temp.média: {media}ºC, Umidade: {umidade}%, Vento: {vento}m/s')

                        elif escolha_opcao_1 == 2:
                        #Exibe no prompt apenas data e dados de precipitação.
                            tipo_dados = "precip"
                            banco_tupla = intervalo_de_dados(dados, mes_inicial, mes_final, ano_inicial, ano_final,tipo_dados)
                            for data, precipitacao in banco_tupla:
                                print(f'Data: {data}, Precipitação {precipitacao}m²')
                        
                        elif escolha_opcao_1 == 3:
                        #Exibe no prompt apenas data e dados de temperatura.
                            tipo_dados = "temp"
                            banco_tupla = intervalo_de_dados(dados, mes_inicial, mes_final, ano_inicial, ano_final,tipo_dados)
                            for data, minima, maxima, media in banco_tupla:
                                print(f'Data: {data}, Temp.mínima: {minima}ºC, Temp.máxima: {maxima}ºC, Temp.média: {media}ºC')

                        elif escolha_opcao_1 == 4:
                        #Exibe no prompt apenas dat, dados de umidade e vento.
                            tipo_dados = "umidade_vento"
                            banco_tupla = intervalo_de_dados(dados, mes_inicial, mes_final, ano_inicial, ano_final,tipo_dados)
                            for data, umidade, vento in banco_tupla:
                                print(f'Data: {data}, Umidade: {umidade}%, Vento: {vento}m/s')

                    #até que algo seja digitado, impede que um novo loop inicie no promtp e o encha de texto.
                        continuar = input("Insira qualquer caracter para dar continuidade: ")
                        if continuar:
                            limpar_tela()
                            break

                    else:
                        limpar_tela()
                        print(f'você inseriu: {escolha_opcao_1}, mas esta não é uma opção válida.\n'
                            'Por favor, digite um valor entre 1 e 4.\n'
                            '- Digite "1" para ver todos os dados\n'
                            '- Digite "2" para ver apenas os dados de precipitação\n'
                            '- Digite "3" para ver apenas os dados de temperatura\n'
                            '- Digite "4" para ver apenas os dados de umidade e vento\n'
                            )
                        escolha_opcao_1 = input("Digite sua escolha: ")
                        continue
                except:
                    limpar_tela()
                    print(f'você inseriu: {escolha_opcao_1}, mas esta não é uma opção válida.\n'
                        'Por favor, digite um valor entre 1 e 4.\n'
                        '- Digite "1" para ver todos os dados\n'
                        '- Digite "2" para ver apenas os dados de precipitação\n'
                        '- Digite "3" para ver apenas os dados de temperatura\n'
                        '- Digite "4" para ver apenas os dados de umidade e vento\n'
                        )
                    escolha_opcao_1 = input("Digite sua escolha: ")
                    continue
                
        elif opcao == '2':
            limpar_tela() 
            m_chuvoso = mes_mais_chuvoso(dados)
            print(f'A data mais chuvosa dos dados coletados, que contempla de 01/01/1967 até 10/07/2016, foi {m_chuvoso}')

            #até que algo seja digitado, impede que um novo loop inicie no promtp e o encha de texto.
            continuar = input("Insira qualquer caracter para dar continuidade: ")
            if continuar:
                limpar_tela()

        elif opcao == '3':
            limpar_tela()
            print('Para saber a média da temperatura mínima de um determinado mês, preciso que você me informe o mês desejado\n'
            'Lembre-se de usar 1 para Janeiro, 2 para Fevereiro, 3 para Março e assim por diante.'
            )
            mes_desejado = input("Insira o mês desejado: ")
            #Tratamento de dados: Permite apenas números entre 1 e 12
            while True:
                try:
                    mes_desejado = int(mes_desejado)
                    if 1 <= mes_desejado <= 12:
                        break
                    else:
                        limpar_tela()
                        print(f'você inseriu {mes_desejado} mas este é um valor inválido.\n'
                            'Por favor, digite um valor entre 1 e 12 (De Janeiro a Dezembro)')
                        mes_desejado = input("Insira o mês desejado: ")
                except:
                    limpar_tela()
                    print(f'você inseriu {mes_desejado} mas este é um valor inválido.\n'
                        'Por favor, digite um valor entre 1 e 12 (De Janeiro a Dezembro)')
                    mes_desejado = input("Insira o mês desejado: ")
            #Executa função:
            media_minima = media_temperatura_min_por_mes(dados, mes_desejado)

            #Resposta da Questão C
            medial_anual_temp_minima = 0
            cont_temp_minima = 0
            limpar_tela()
            print(f'O mês selecionado foi {meses_por_extenso[mes_desejado]}')
            for ano in range(2006, 2017):
                chave = f"{mes_desejado}/{ano}"
                nome_mes = meses_por_extenso[mes_desejado]

                if chave in media_minima:
                    medial_anual_temp_minima += media_minima[chave]
                    cont_temp_minima += 1
                    
                    print(f"A média de {nome_mes} de {ano} foi de: {media_minima[chave]:.2f} °C")
                else:
                    print(f"Não há dados para {nome_mes} de {ano}")
            #Gráfico da questão D
            grafico_temp_minima(media_minima,nome_mes)
            #Resposta questão E
            print(f"A média entre os anos de 2006 e 2016 foi de {medial_anual_temp_minima/cont_temp_minima:.2f} °C")
          
            #até que algo seja digitado, impede que um novo loop inicie no promtp e o encha de texto.
            continuar = input("Insira qualquer caracter para dar continuidade: ")
            if continuar:
                 limpar_tela()
        
        # Encerra o programa    
        elif opcao.lower() == "sair":
            print('Obrigado por testar este programa.')
            break 
        #Informa input inválido
        else:
            limpar_tela()
            print(f'Você inseriu {opcao.upper()} e esta não é uma opção válida. Por favor favor, insira uma opção válida!\n')

elif inicio.lower() == "n":
      limpar_tela()
      print('Que pena que você não quer testar o programa, até a próxima!')
    
else:
    limpar_tela()
    print("Hum, falhei nas instruções. Recomeça o programa e digita 'S' ou 'N'\n"
          "Eu sei que poderia colocar um loop aqui, mas presta atenção nas intruções que assim você não terá retrabalho."
          )
