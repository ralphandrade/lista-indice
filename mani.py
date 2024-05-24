# lista de nomes
nomes= ['Maria', 'João','Juliana','Pedro','Rafael','Zamis','Eduardo','Eliane','Alfredo','Beatriz','Carlos', 'Fabio','Lais','Orlando','Patricia']

# usuário informa o nome que deseja pesquisar
nome = input('Digite o nome a ser pesquisado: ')

# Verifica se o nome está na lista ou não
try:
    #retorna o índice do nome pesquisado
    indice = nomes.index(nome)
    print(f'Nome encontrado: {nome} no indice {indice}.')
except:
    print(f'{nome} não encontrado na lista')