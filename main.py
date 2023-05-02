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
    peca = {}
    codigo += 1
    peca['Codigo'] = codigo
    print(f'Código da peça: {codigo:03d}') # saída: 001
    peca['Nome'] = str(input('Por favor, entre com o NOME da peça: '))
    peca['Fabricante'] = str(input('Por favor, entre com o FABRICANTE da peça: '))
    peca['Valor'] = float(input('Por favor, entre com o VALOR da peça: '))
    pecas.append(peca)
    break
# fim da função cadastrarPeca()

# inicio da função consultaPeca()
def consultaPeca():
  while True:
    print('Escolha a opção desejada:')
    print('1 - Consultar todas as peças')
    print('2 - Consultar peça por Código')
    print('3 - Consultar peça por Fabricante')
    print('4 - Retornar')
    opcUser = int(input('>>> '))
    if opcUser == 1:
      for e in pecas:
        print('--'*10)
        for i,j in e.items():
          print(f'{i}: {j}')
        print('--'*10)
    elif opcUser == 2:
      codigoProduto = int(input('Digite o CÓDIGO da peça: ')) 
      for peca in pecas:
        if peca['Codigo'] == codigoProduto:
          for i,j in peca.items():
            print(f'{i}: {j}')          
    elif opcUser == 4:
      break
      
      
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
  print('3 - Remover peças')
  print('4 - Sair')
  opUser = int(input('>>> '))
  if opUser == 1:
    print('Voce selecionou a opção de Cadastrar Peças')
    cadastrarPeca()
  elif opUser == 2:
    print('Voce selecionou a opção de Consultar Peças')
    consultaPeca()
  elif opUser == 3:
    print('Voce selecionou a opção de Remover Peças')
    removerPeca()
  elif opUser == 4:
    break
    
# fim do main