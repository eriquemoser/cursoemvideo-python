import math

ang = float(input('Digite o ângulo que você deseja: '))

print('o SENO de {:.2f} é: {:.2f}'.format(ang,math.sin(math.radians(ang))))
print('o COSSENO de {:.2f} é: {:.2f}'.format(ang,math.cos(math.radians(ang))))
print('a TANGENTE de {:.2f} é: {:.2f}'.format(ang,math.tan(math.radians(ang))))