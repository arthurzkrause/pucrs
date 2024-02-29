import os
#Função para limpar o Terminal
def limpar_tela():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

limpar_tela()

#Introdução
print(
'Olá, bem-vindo ao programa de Análise Meteorológica - Fase 1\n'
'O programa está em sua primeira fase e foi escrito por Arthur Zasso Krause\n'
'para a cadeira de Lógica e Programação de Computadores\n'
'Neste programa, será requisitado a inserção de dados meteorológicos e será feita a análise dos mesmos.\n'
)
inicio = input('Podemos iniciar? Digite "S" para sim e "N" para não: ')
if inicio.lower() == "s":
      limpar_tela()

#Escrita dos meses para melhor visualização ao realizar input e corrigir dados
      meses_por_extenso = {
    "1": "Janeiro",
    "2": "Fevereiro",
    "3": "Março",
    "4": "Abril",
    "5": "Maio",
    "6": "Junho",
    "7": "Julho",
    "8": "Agosto",
    "9": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro",
}
#Dicionário para armazenar dados
      meses_e_temperaturas = {}
      meses_lista_validacao = []
#Valida os dados para encerar a repetição
      lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

      while True:
            entrada_mes = input('Utilize os números de 1 a 12 para identificar o mês e caso se perca, digita "meses.\nDigite o mês (e.g 1 corresponde a Janeiro):')
#Entrega a possibilidade ao usuário de ver o dict caso se perca
            if entrada_mes.lower() == "meses":
                 limpar_tela()
                 if meses_lista_validacao == []:
                      print('Nenhum mês cadastrado')
                 else:
                      print(f'Você já cadastrou as informações: {meses_e_temperaturas}')
#Confirma se o input é um número e informa ao usuário a melhor forma de notação
            try:
                  entrada_mes = int(entrada_mes)
            except:
                  if entrada_mes.lower() == "meses":
                       continue
                  else:
                       print('Insira apenas números entre 1 e 12, correspondentes de Janeiro até Dezembro.')
                       continue
            
#Confirma se o input está entre 1 e 12 e informa ao usuário caso não seja
            if 1 <= entrada_mes <= 12:
#Confere se o mês já foi digitado e caso seja, questiona se deseja corrigir a temperatura                     
                  if entrada_mes in meses_lista_validacao:
                        limpar_tela()
                        print(f'Você já digitou informações sobre o mês de {meses_por_extenso[str(entrada_mes)]}. Tempretura de: {meses_e_temperaturas[entrada_mes]}ºC\nDeseja corrigí-lo?'
                              )
                        duplicada = input('Digite "S" para sim e "N" para não: ')
                        if duplicada.lower() == "s":
                              ... #Mantive "..." para pular para próxima parte. Ao utilizar break o código para.
                        elif duplicada.lower() == "n":
                              limpar_tela()
                              continue
                        else:
                              limpar_tela()
                              print('Digite apenas "S" ou "N"')
                              continue
#Entrada da Temperatura e validação 
                  try:
                        limpar_tela()
                        entrada_temperatura = input(f'Digite a temperatura do mês {meses_por_extenso[str(entrada_mes)]} em graus celcius: ')
                        entrada_temperatura = float(entrada_temperatura.replace(",","."))
                        if -60 <= entrada_temperatura <= 50:
                              meses_e_temperaturas[entrada_mes] = entrada_temperatura
                              limpar_tela()
                        else:
                              print('Digite apenas números entre "-60" e "50ºC". (E.g 28,7)')
                              continue
                  except:
                        print('Erro desconhecido') #Sei que não é a melhor opção de uso
                        break
                        
#Caso ainda não tenha sido digitado, adiciona a entrada em uma lista para confirmar se o número já foi digitado a fim de corrigí-lo
                  if entrada_mes not in meses_lista_validacao:
                        meses_lista_validacao.append(entrada_mes)
                  else:
                        continue
            else:
                 print('Insira apenas números entre 1 e 12, de Janeiro até Dezembro.')
                 
#Finaliza a repetição após todos os meses seres inseridos 
            if all(numero in meses_lista_validacao for numero in lista_numeros):
                  break

#Cálculo de média máxima anual
      limpar_tela()
      print('A análise constatou que:')
      media_maxima_anual = 0
      for temperatura in meses_e_temperaturas.values():
            media_maxima_anual += temperatura
      media_maxima_anual = media_maxima_anual/12
      print(f'A temperatura média máxima anual foi de {media_maxima_anual:.2f}ºC')

      #Meses escaldantes
      escaldante = 0
      for temperatura in meses_e_temperaturas.values():
           if temperatura > 33:
            escaldante += 1
#Seleciona plural
      if escaldante != 1:
            print(f'Houve {escaldante} meses com temperatura a cima da média de 33ºC')
      else:
           print(f'Houve {escaldante} mês com temperatura a cima da média de 33ºC')


      #Mês mais escaldante do ano
#Ordena os valores do Dict, o seleciona e imprime o mês correspondente com maior e menor temperatura
      meses_ordenados = sorted(meses_e_temperaturas.values())
      maior_temperatura = meses_ordenados[-1]
      menor_temperatura = meses_ordenados[0]

      for mes, temperatura in meses_e_temperaturas.items():
            if temperatura == maior_temperatura:
                  maior_mes = mes
            if temperatura == menor_temperatura:
                  menor_mes = mes   
      print(f"O mês com a maior temperatura foi {meses_por_extenso[str(maior_mes)]} com {maior_temperatura}ºC, já o de menor temperatura foi {meses_por_extenso[str(menor_mes)]} com {menor_temperatura}ºC.")

elif inicio.lower() == "n":
      limpar_tela()
      print('Que pena que você não quer, até a próxima!')
    
else:
    limpar_tela()
    print("Hum, falhei nas instruções. Recomeça o programa e digita 'S' ou 'N'")
