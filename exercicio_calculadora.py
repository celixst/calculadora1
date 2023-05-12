print('Seja bem-vindo(a) à calculadora. Siga as instruções a seguir.')

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite a operação que deseja fazer (+-*/): ')

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0
    numero_final = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou mais números digitados são inválidos.')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    try:  
        if operador == '+':
            numero_final = numero_1_float + numero_2_float
        elif operador == '-':
            numero_final = numero_1_float - numero_2_float
        elif operador == '*':
            numero_final = numero_1_float * numero_2_float
        elif operador == '/':
            numero_final = numero_1_float / numero_2_float
        print(f'O resultado final é {numero_final}')
    except:
        print('Você não digitou um operador válido')
        continue

    sair = input('Quer sair? [s] para sim ').lower().startswith('s')

    if sair is True:
        break
