# inicio da função cadastrarPeca()
def cadastrarPeca():
  # Variável global para armazenar o código da peça
  global codigo
  # Loop infinito para o cadastro de peças
  while True:
     # Dicionário para armazenar as informações da peça, inicialmente vazio.
    peca = {}
    # Contador irá incrementar o código da peça
    codigo += 1
    # Adiciona o código, nome, fabricante e valor da peça ao dicionário de acordo com o input do usuário
    peca['Codigo'] = int(codigo)
    print(f'Código da peça: {codigo:03d}') # saída: 001
    peca['Nome'] = str(input('Por favor, entre com o NOME da peça: ')).lower()
    peca['Fabricante'] = str(input('Por favor, entre com o FABRICANTE da peça: ')).lower()
    peca['Valor'] = float(input('Por favor, entre com o VALOR da peça: '))
    # Adiciona o dicionario peça à uma lista
    pecas.append(peca)
    # Encerra o loop
    break
# fim da função cadastrarPeca()

# inicio da função consultaPeca()
def consultaPeca():
  # Mais um loop infinito, agora para a consulta de peças
  while True:
    # Exibe as opções de consulta de peças
    print('Escolha a opção desejada:')
    print('1 - Consultar todas as peças')
    print('2 - Consultar peça por Código')
    print('3 - Consultar peça por Fabricante')
    print('4 - Retornar')
    # Lê a opção escolhida pelo usuário
    opcUser = int(input('>>> '))
    # Verifica cada opção escolhida pelo usuário
    if opcUser == 1:
      # Loop para exibir todas as peças cadastradas de forma limpa
      for valor in pecas:
        print('--'*10)
        for chaves, valores in valor.items():
          print(f'{chaves}: {valores}')
        print('--'*10)
    elif opcUser == 2:
      # Pede ao usuário o código da peça a ser consultada
      codigoProduto = int(input('Digite o CÓDIGO da peça: ')) 
      # Loop para buscar a peça pelo código e exibi-la de forma limpa
      for peca in pecas:
        if peca['Codigo'] == codigoProduto:
          print('--'*10)
          for chaves, valores in peca.items():
            print(f'{chaves}: {valores}')          
          print('--'*10)
    elif opcUser == 3:
      # Pede ao usuário o fabricante da peça a ser consultada
      fabricanteProduto = str(input('Digite o FABRICANTE da peça: ')).lower()
      # Loop para buscar a peça pelo fabricante e exibi-la
      for peca in pecas:
        if peca['Fabricante'] == fabricanteProduto:
          print('--'*10)
          for chaves, valores in peca.items():
            print(f'{chaves}: {valores}')          
          print('--'*10) 
    # opção 4 - retornar ao menu principal, encerra o loop atual
    elif opcUser == 4:
      break
# fim da função consultaPeca()

# inicio da função removerPeca()
def removerPeca():
  codigoProduto = int(input('Digite o CÓDIGO da peça a ser removida: '))
  # para cada cadastro (dicionario) de peça na lista de peças
  for peca in pecas:
    # se o código do cadastro for igual ao código inserido pelo usúarios, remova o cadastro da peça da lista
    if peca['Codigo'] == codigoProduto:
      pecas.remove(peca)
# fim da função removerPeca() 

# inicio do main
codigo = 0
pecas = []
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