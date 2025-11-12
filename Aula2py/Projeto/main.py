# Criar variável que pergunte o nome do cliente 
nome_cliente = input('Qual é o seu nome? Insira seu nome: ')

print(f'Seja Bem-Vindo(a) {nome_cliente}!')

# Criar variável que vai falar o nome do filme 
nome_filme = input('Insira o nome do filme que você gosta:')

print(f'Voce escolheu o filme {nome_filme}')

# Criar variável que vai falar o valor do ingresso
    # Ingresso - Inteira
    # Ingresso - Meia 
valor_ingresso_inteiro = 30.00
valor_ingresso_meia = valor_ingresso_inteiro / 2

print(f'O valor do ingresso inteiro e {valor_ingresso_inteiro} e a meia e R${valor_ingresso_meia}')

# Criar variável que vai perguntar a idade do cliente
idade_cliente = input('Insira sua idade: ')
idade_cliente = int(idade_cliente)

print(f'Sua idade é {idade_cliente}')

# Criar texto falando as informações passada
 
# Seja bem vindo(a) nome da pessoa
# O filme que está em cartaz é nome do filme 
# O ingresso inteira está tantos reais e o meia tantos reais 
nome_cliente = input('Qual é o seu nome? Insira seu nome: ')
nome_filme = 'Sherlock Holmes - O Jogo das Sombras'
valor_ingresso_inteiro = 30.00
valor_ingresso_meia = valor_ingresso_inteiro / 2

print(f'Seja Bem-Vindo(a) {nome_cliente}!')
print(f'O filme que esta em cartaz e {nome_filme}')
print(f'O valor do ingresso inteiro e {valor_ingresso_inteiro} e a meia e R${valor_ingresso_meia:.2f}')

# Criar variável que vai perguntar quantos ingressos e armazenar
quant_ingressos = input('Quantos ingressos voce quer comprar: ')
quant_ingressos = int(quant_ingressos)
idade_cliente = input('Insira sua idade: ')
idade_cliente = int(idade_cliente)
valor_ingresso_inteiro = 30.00
valor_ingresso_meia = valor_ingresso_inteiro / 2

print(f'Sua idade é {idade_cliente}')
print(f'voce comprou {quant_ingressos} ingressos')

if idade_cliente <= 24 or idade_cliente >= 60:
    valor_final = quant_ingressos * valor_ingresso_meia
    
    #print(f'Seu ingresso custou R${valor_final:.2f}')

else: 
    valor_final = quant_ingressos * valor_ingresso_inteiro

    #print(f'Seu ingresso custou R${valor_final:.2f}')
 
if quant_ingressos <= 3:
    valor_final *= 0.95

elif quant_ingressos <= 5:
    valor_final *= 0.90

elif quant_ingressos <= 10:
    valor_final *= 0.80

else:
    valor_final *= 0.70

print(f'Sua compra saiu o total de R$ {valor_final:.2f}')