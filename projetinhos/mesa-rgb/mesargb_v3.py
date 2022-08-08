import serial

#//////////////////////////////////////////////////////////// Efeitos:
def cor():
    try:
        print('\n\t(0 a 255)\n')
        r = int(input('\tR> '))
        g = int(input('\tG> '))
        b = int(input('\tB> '))

        if r>255 or g>255 or b>255:
            r = 255
            g = 255
            b = 255
            print(f'\n Aviso: 255 é o máximo, exibindo Branco!\n')
        elif r<0 or g<0 or b<0:
            r = 0
            g = 0
            b = 0
            print(f'\n Aviso: 0 é o mínimo, Luz Apagada!\n')
        return f'1,{r},{g},{b}'
    except:
        print('\n Cor inválida, exibindo Branco!')
        return '1,255,255,255'
#////////////////////////////////////////////////////
def fade():
    try:
        delay = int(input('\n Delay entre cores(ms): '))
        if delay > 100:
            delay = 100
            print(f'\n Aviso: {delay}ms é o máx.!\n')
        elif delay < 1:
            delay = 1
            print(f'\n Aviso: {delay}ms é o min.!\n')

        return f'2,{delay}'
    except:
        print('\n Delay inválido, exibindo Fade(1ms)!')
        return '2,1'
#////////////////////////////////////////////////////
def police():
    try:
        delay = int(input('\n Delay entre cores(ms): '))
        if delay > 10:
            delay = 10
            print(f'\n Aviso: {delay}ms é o máx.!\n')
        elif delay < 1:
            delay = 1
            print(f'\n Aviso: {delay}ms é o min.!\n')

        return f'3,{delay}'
    except:
        print('\n Delay inválido, exibindo Police(1ms)!')
        return '3,1'
#////////////////////////////////////////////////////
def strobe():
    try:
        hz = int(input('\n Frequência entre Flash(Hz): '))
        if hz > 60:
            hz = 60
            print(f'\n Aviso: {hz}hz É a freq. máx.!\n')
        elif hz < 1:
            hz = 1
            print(f'\n Aviso: {hz}hz É a freq. min.!\n')
        corrigido = round(1000/hz)
        return f'4,{corrigido}'
    except:
        print('\n Freq. inválida, executando Strobe(1Hz)!')
        return '4,1000'
#//////////////////////////////////////////////////////////// Conecta BT pela porta 'COM8' (pendrive bt)
while True:
    try:
        print('\n Tentativa de conectar...',end=' ')
        ser = serial.Serial("COM7",9600)
        print('Conectado!')
        break
    except:
        print('\n Não consegui conectar ainda...')
#//////////////////////////////////////////////////////////// Menu:
while True:
    modo = input('\n 1>Cor Estática;\n 2>Fade;\n 3>Police;\n 4>Strobe;\n 5>Sair;\n -> ')
    #os.system('cls')
    if modo == '1':
        comando = cor()
        ser.write(comando.encode())
        print(f'\n Comando enviado: "{comando}"')

    elif modo == '2':
        comando = fade()
        ser.write(comando.encode())
        print(f'\n Comando enviado: "{comando}"')

    elif modo == '3':
        comando = police()
        ser.write(comando.encode())
        print(f'\n Comando enviado: "{comando}"')

    elif modo == '4':
        comando = strobe()
        ser.write(comando.encode())
        print(f'\n Comando enviado: "{comando}"')

    elif modo == '5':
        ser.close()
        break
    else:
        print('\n Opção inválida!')
