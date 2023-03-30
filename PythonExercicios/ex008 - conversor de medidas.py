m=float(input('Digite uma distância em metros: '))
km=m/1000
hm=m/100
dam=m/10
dm=m*10
cm=m*100
mm=m*1000

print('{} metros equivale a: \n'
      '-> {} Quilômetros \n'
      '-> {} hectômetros \n'
      '-> {} decametros \n'
      '-> {} decimetros \n'
      '-> {} centímetros \n'
      '-> {:.0f} milímetros'.format(m,km,hm,dam,dm,cm,mm))