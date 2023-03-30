velocidade = float(input('Indique a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você estava acima da velocidade e foi multado em R${}!'.format(multa))
else:
    print('Parabéns, você estava dentro da velocidade permitida.')