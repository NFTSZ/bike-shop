'''Escolha a opção desejada:
      1 - Cadastrar peças
      2 - Consultar Peças
        1) Consultar todas as peças
        2) Consultar Peças por código
        3) consultar peças por fabricante
        4) retornar
      3 - remover peças
      4 - SAIR
      
        for peca, valor in pecas.items():
        print(peca, valor)'''
      
# inicio da função cadastrarPeca()
def cadastrarPeca():
    global codigo
    codigo += 1
    print(f'Código da peça: 00{codigo}')
    nomePeca = str(input('Por favor, entre com o NOME da peça: '))
    fabricantePeca = str(input('Por favor, entre com o FABRICANTE da peça: '))
    valorPeca = float(input('Por favor, entre com o VALOR da peça: '))
    
    pecas = {'Código': codigo, 'Nome:': nomePeca, 'Fabricante:': fabricantePeca, 'Valor:': valorPeca}
 
    
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
print('Bem vindo(a) ao Controle de Estoque da Bicicletaria da Naftaly Benedita Souza')

cadastrarPeca()
# fim do main