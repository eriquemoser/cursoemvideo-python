v = input('Digite uma variável: ')
print('O tipo da variável é: ',type(v))

print('Só tem espaços? ', v.isspace())
print('Pode ser numérico? ',v.isnumeric())
print('Pode ser string? ',v.isalpha())
print('Pode ser alpha numérico? ',v.isalnum())
print('Pode ser string maiúscula? ',v.isupper())
print('Pode ser string minúscula? ',v.islower())
print('Está capitalizada? ', v.istitle())