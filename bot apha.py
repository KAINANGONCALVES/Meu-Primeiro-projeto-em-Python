# inicio do sistema - apha
from random import choice

print('Seja muito bem Vindo ao Sistema:)')

# Perfil-inicio
nome = str(input('Qual é seu nome?: ')).strip().upper()
plano = int(input('qual o valor do seu plano R$'))
print('Qual atendimento você procura?: ')
# Perfil-fim

# Escolha de atendimento - inicio
print('-=-' * 20)
print('1°atendimento - multa '
      '\n2°atendimento - Pagamento')
print('-=-' * 20)
# Escolha de atendimento - final

N = int(input('Qual atendimento é sua escolha?: '))
print('-=-' * 20)

# atendimento 1 - inicio
if N == 1:
    print('Seja bem - vindo ao sisteme de multa {} '.format(nome))
    print('-' * 60)
    if nome == 'KAINAN':
        print('Verificamos que seu plano é de R${:.2f}'
              '\n\033[0:31m e voce tem um pagamenton pendente\033[m.'.format(plano))
    else:
        print('Virificamos que seu plano é de R${:.2f}'
              '\n\033[0:32m e não tem pamento pendente.\033[m'.format(plano))
# atendimento 1 - fim

# atendimento 2 - inicio
if N == 2:
    print('Seja bem - vindo á Pagamentos {}'
          '\nA multa é somada pelo dias que estão pendentes'.format(nome))
    lista = [2, 3, 5, 6, 8, 9]
    dias = choice(lista)
    if nome == 'KAINAN':
        print('O pagamento está atrasado a {} dias'
              '\nO valor da multa é de R$3,00 por dia!'.format(dias))
        pagar = (plano + dias * 3)
        print('O total que você deve pagar é R${:.2f} já somado com o atraso de {} dias '.format(pagar, dias))
    else:
        print('Seu pagamento está em dia dia')
# atendimento 2 - fim
print('-=-' * 20)
