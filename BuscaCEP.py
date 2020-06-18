import requests

def BuscaCep():
    print('#################')
    print('### BUSCA CEP ###')
    print('#################\n')

    cep = input('Digite o CEP a ser buscado: ')
    if len(cep) != 8:
        print(' CEP deve conter 8 numeros')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    resultJson = request.json()
    if 'erro' in request.json():
        print('{}: CEP Invalido'.format(cep))
    else:
        print ('-->> CEP encontrado <<--\n')
        print('CEP: {}'.format(resultJson['cep']))
        print('Rua: {}'.format(resultJson['logradouro']))
        print('Bairro: {}'.format(resultJson['bairro']))
        print('Cidade: {}'.format(resultJson['localidade']))
        print('Estado: {}'.format(resultJson['uf']))

    replay = int(input('\n Deseja buscar um novo CEP? \n 1 - Para sim \n 2 - Para não \n'))
    if replay == 1:
        BuscaCep()
    else: 
        print('Saindo...')

if __name__ == "__main__":
    BuscaCep()