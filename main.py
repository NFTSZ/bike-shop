'''Escolha a opção desejada:
      1 - Cadastrar peças
      2 - Consultar Peças
        1) Consultar todas as peças
        2) Consultar Peças por código
        3) consultar peças por fabricante
        4) retornar
      3 - remover peças
      4 - SAIR
              
      for e in pecas:
        for i,j in e.items():
          print(f'{i}: {j}')
          
      encerrar = int(input('>>'))
      if encerrar == 1:
        break
      else:
        continue'''
        
# inicio da função cadastrarPeca()
def cadastrarPeca():
    global codigo
    while True:
      codigo += 1
      peca['Codigo'] = '{:03d}'.format(codigo)
      print(f'Código da peça: {codigo:03d}') # saída: 001
      peca['Nome'] = str(input('Por favor, entre com o NOME da peça: '))
      peca['Fabricante:'] = str(input('Por favor, entre com o FABRICANTE da peça: '))
      peca['Valor'] = float(input('Por favor, entre com o VALOR da peça: '))
      pecas.append(peca.copy())
      break
# fim da função cadastrarPeca()

# inicio da função consultaPeca()
def consultaPeca():
    print('')
# fim da função consultaPeca()

# inicio da função removerPeca()
def removerPeca():
    print('')
# fim da função removerPeca() 

# inicio do main
codigo = 0
pecas = []
peca = {}
print('Bem vindo(a) ao Controle de Estoque da Bicicletaria da Naftaly Benedita Souza')
while True:
  print('Escolha a opção desejada:')
  print('1 - Cadastrar peças')
  print('2 - Consultar Peças')
  print('3 - remover peças')
  print('4 - SAIR')
  opUser = int(input('>>> '))
  if opUser == 1:
    cadastrarPeca()
  elif opUser == 2:
    consultaPeca()
# fim do main