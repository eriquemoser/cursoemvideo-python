largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

area = largura * altura

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m². \n'
      'Para pintar essa parede, você precisará de {}l de tinta.'.format(largura,altura,area,area/2))