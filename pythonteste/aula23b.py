try: #o que vai tentar fazer
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))

    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except (ZeroDivisionError):
    print('Não é possível dividir um número por zero')
except (KeyboardInterrupt):
    print('O usuário preferiu não informar os dados')
except Exception as erro: #o que vai aparecer se der errado
    print(f'O problema encontrado foi {erro.__cause__}')
else: #o que vai aparecer se der certo
    print(f'O resultado é {r:.2f}')
finally: #acontece sempre
    print('Volte sempre')