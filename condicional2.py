temperatura = int(input('Digita la temperatura: '))
gradosAlcohol = int(input('Digitar los grados de alcohol: '))

if temperatura > 50 or gradosAlcohol > 5:
    print('alarma')
else:
    print('Normal')