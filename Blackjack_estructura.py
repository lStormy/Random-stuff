#----------------------#
import Blackjack_objetos
#----------------------#

#1. Declaración del jugador:
jugador1 = Blackjack_objetos.Jugador('1')
dealer = Blackjack_objetos.Jugador('Dealer')

#2. Un While que marque hasta que termine el juego
while True:    
    #3. Repartimos dos cartas al jugador:
    Dealer = Blackjack_objetos.Mazo()
    Dealer.mezclar()
    for i in range(2):
        jugador1.agregar(Dealer.repartir_una())
        dealer.agregar(Dealer.repartir_una())
    
    #4: Apuestas: 
    print(f'¿Cuanto quiere apostar? su presupuesto es: {jugador1.fichas}')
    while True:
        try: 
            apuesta = int(input('Ingrese cuanto quiere apostar: '))
        except:
            print ('Parece que no ingreso un valor permitido, intente devuelta.')
        else: 
            if apuesta > jugador1.fichas:
                print ('No tiene suficientes fichas')
            else: 
                print ('¡Entendido!')
                break
    jugador1.apostar(apuesta)
    print (f'Sus fichas restantes son: {jugador1.fichas}')
    
    #5. Calcular la suma de las cartas del jugador
    print ('-------------------------------------------')
    print (f'Las cartas del dealer son: \n 1.{dealer.mano[0]} \n 2. ??? ')
    print ('-------------------------------------------')
    print ('Sus cartas son: ')
    cantidad = 0
    for i in range(0,len(jugador1.mano)):
        cantidad += 1
        print (f'La carta numero {cantidad} es: {jugador1.mano[i]}')
    print ('-------------------------------------------')
    print(f'La suma de sus cartas es: {jugador1.suma()}')
    print ('-------------------------------------------')
    
    #6. Preguntar si quiere agregar más cartas: 
    while True: 
        hit = input ('Quiere agregar cartas?, s = si n = no: ')
        if hit == 's':
            jugador1.agregar(Dealer.repartir_una())
            print ('-------------------------------------------')
            print (f'la carta agregada es: {jugador1.mano[-1]}')
            print(f'la suma de sus cartas es: {jugador1.suma()}')
            print ('-------------------------------------------')
            if jugador1.suma() > 21: 
                break
        elif hit == 'n':
            break
        else: 
            print ('Oops parece que no ingresaste un caracter correcto, vuelve a intentar.')
    print ('============================================================')
    
    #7. Determinar si se pasa o no de 21: 
    if jugador1.suma() > 21:
        print (f'El jugador {jugador1.nombre} perdió. La suma de sus cartas pasó de 21')
        print(f'El jugador quedó con: {jugador1.fichas} fichas')
        if jugador1.fichas == 0:
            break
        else: 
            continue
    else: 
        print ('============================================================')
        print ('Le toca a la casa ahora:')
        print (f'Las cartas del Dealer son: \n 1. {dealer.mano[0]} \n 2. {dealer.mano[1]}')
        print (f'Y la suma de sus cartas es: {dealer.suma()}')
        if jugador1.suma() >= dealer.suma():
            while dealer.suma() <= jugador1.suma():
                dealer.agregar(Dealer.repartir_una())
                print ('-----------------------------------------------')
                print (f'La carta agregada es {dealer.mano[-1]}')
                print ('-----------------------------------------------')
                print (f'Ahora la suma de sus cartas es: {dealer.suma()}')
                if dealer.suma() > 21:
                    print (f'La suma de las cartas es: {dealer.suma()}')
                    print (f'Gana el jugador {jugador1.nombre}. La suma de las cartas del Dealer supero el máximo')
                    jugador1.gana(apuesta)
                    print (f'Como ganó el jugador sus fondos son: {jugador1.fichas}')
                    break
                elif dealer.suma() > jugador1.suma():
                    break
        elif dealer.suma() > jugador1.suma():
            print('El jugador pierde, gana la casa')
            print(f'El jugador quedó con: {jugador1.fichas} fichas')
            if jugador1.fichas == 0:
                break
            else: 
                continue
    #8. Preguntar si quiere seguir jugando y apostando sus fichas:
    while True:
        print('========================================================================')
        seguir = input('¿Quiere seguir jugando y apostar sus fichas? s = si n = no: ')
        if seguir == 's':
            print ('===================================================================')
            break
        elif seguir == 'n':
            print ('===================================================================')
            break
        else:
            print ('Parece que no brindó un valor correcto')
    if seguir == 's':
        for i in range(len(jugador1.mano)):
            Dealer.devolver(jugador1.devolver())
        for i in range (len(dealer.mano)):
            Dealer.devolver(dealer.devolver())    
        continue
    else: 
        break