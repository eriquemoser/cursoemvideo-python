peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em mts: '))

imc = peso/(altura*altura)

print('Seu IMC é de {}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Seu peso é ideal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso')
elif 30 <= imc < 40:
    print('Você está com obesidade')
elif imc >=40:
    print('Você está com obesidade mórbida')