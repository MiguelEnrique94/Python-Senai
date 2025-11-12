primeiro_numero = input('Digite o primeiro numero: ')
primeiro_numero = int(primeiro_numero)
segundo_numero = input('Digite o segundo numero: ')
segundo_numero = int(segundo_numero)
terceiro_numero = input('Digite o terceiro numero: ')
terceiro_numero = int(terceiro_numero)


if primeiro_numero >= segundo_numero or primeiro_numero <= segundo_numero:
    print(f'O maior numero digitado é {primeiro_numero} e o menor numero digitado é {segundo_numero}')
elif primeiro_numero >= terceiro_numero or primeiro_numero <= terceiro_numero:
    print(f'O maior numero digitado é {primeiro_numero} e o menor numero digitado é {terceiro_numero}')
elif segundo_numero >= primeiro_numero or segundo_numero <= primeiro_numero:
    print(f'O maior numero digitado é {segundo_numero} e o menor numero digitado é {primeiro_numero}')
elif segundo_numero >= terceiro_numero or segundo_numero <= terceiro_numero:
    print(f'O maior numero digitado é {segundo_numero} e o menor numero digitado é {terceiro_numero}')
elif terceiro_numero >= primeiro_numero or terceiro_numero <= primeiro_numero:
    print(f'O maior numero digitado é {terceiro_numero} e o menor numero digitado é {primeiro_numero}')
elif terceiro_numero >= segundo_numero or terceiro_numero <= segundo_numero:
    print(f'O maior numero digitado é {terceiro_numero} e o menor numero digitado é {segundo_numero}')