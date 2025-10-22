nome_filme = 'Sherlock Holmes - O Jogo das Sombras'
sala_cinema = 'sala dos betinha'
duracao = 100
quant_pessoas = 300
valor_ingresso_inteiro = 30.00
valor_ingresso_meia = valor_ingresso_inteiro / 2
quant_ingressos = input('Quantos ingressos voce quer comprar: ')
quant_ingressos = int(quant_ingressos)
valor_final = quant_ingressos * valor_ingresso_inteiro

print(f'Venham assistir ao filme {nome_filme} na {sala_cinema}')
print(f'Esse filme tem {duracao} min de duracao e o valor do ingresso e de R${valor_ingresso_inteiro}')
print(f'E o valor do ingresso como meia e de R${valor_ingresso_meia}')

print(f'voce comprou {quant_ingressos} ingressos e o valor ficou em: R${valor_final}')

