#Importado:
import random 

#Variables Globales
valores = {'Dos': 2, 'Tres': 3, 'Cuatro': 4, 'Cinco': 5, 'Seis': 6, 
           'Siete': 7, 'Ocho': 8, 'Nueve': 9, 'Diez': 10, 'Jota': 10, 
           'Reina': 10, 'Rey': 10, 'As': 1}
palos = ('Corazones', 'Diamantes', 'Espadas', 'Picas')
numeros = ('Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 
           'Diez', 'Jota', 'Reina', 'Rey', 'As')

#Cartas
class Carta:
    def __init__ (self, palo, numero):
        self.palo = palo
        self.numero = numero
        self.val = valores [numero]
    def valor (self):            
        return (self.val)
    def __str__ (self):
        return f'{self.numero} De {self.palo}'

#Mazo
class Mazo: 
    def __init__ (self): 
        self.cartas = []
        for palo in palos:
            for numero in numeros:
                carta_creada = Carta(palo,numero)
                self.cartas.append(carta_creada)
    def devolver(self,nueva_carta):
        if type(nueva_carta) == type([]):
            self.cartas.extend(nueva_carta)
        else:
            self.cartas.append(nueva_carta)
    def mezclar (self):
        random.shuffle (self.cartas)
    def repartir_una (self):
        return self.cartas.pop()


class Presupuesto:
    def __init__(self):
        self.fichas = 1 
    def apostar (self, apuesta):
        if apuesta > self.fichas:
            print('Fichas insuficientes')
        else:
            self.fichas -= apuesta
            return self.fichas
    def gana (self, apostado): 
        ganado = apostado * 2
        self.fichas += ganado
        return self.fichas
    def __str__(self):
        return (f'Las fichas son {self.fichas}')

class Jugador (Presupuesto):
    def __init__ (self, nombre):
        self.nombre = nombre
        self.mano = []
        self.fichas = 1
    def agregar (self, nueva_carta):
        if type(nueva_carta) == type([]):
            self.mano.extend(nueva_carta)
        else:
            self.mano.append(nueva_carta)
    def devolver (self):
        return self.mano.pop(0)
    def suma (self):
        resultado = 0
        for i in self.mano:
            aux = 0
            if i.valor() == 1 and resultado < 11: 
                aux = 11
                resultado += aux
            else:
                resultado += i.valor()
            if aux == 11 and resultado > 21:
                resultado -= 10
                aux = 0
        return resultado    
    def __str__ (self):
        return (f'El jugador {self.nombre} tiene {len(self.mano)} cartas')

#codigos
def silla():
	print ('           __')	
	print ('         /   /')
	print ('        /   /')
	print ('       -----')
	print ('      /|   |')
	print ('     / | _ |')
	print ('      /   /')
	print ('     /   /')

def petu ():
	print ('     __      __  ')
	print('    /  \    /  \ ')
	print ('   /    \  /    \ ') 
	print ('   \     \/     / ') 
	print ('    \          /')
	print ('     \        /')
	print ('      \      /')
	print ('       \    /')
	print ('        \  /')
	print ('         \/')
ronda = 0
#=====================================================================================#
#0. Configurar el menu:

def menu():
    while True:
        try:
            print ('-----------------------------------')
            modo = int(input ('1: Como jugar \n2: Blackjack \nElija un modo que quiera jugar: '))
            print ('-----------------------------------')
        except:
            print ('Error')
        else: 
            if modo not in (1,2): 
                print ('Ingrese un modo valido')
            else:
                print (f'Elegió el modo: {modo}')
                break
    return modo

def como_jugar():
    print('==============================================================================')
    print('1. Usted va a recibir 2 cartas')
    print('2. El objetivo es que suma de sus cartas debe acercarse lo máximo posible a 21.')
    print('3. Gana si la suma de sus cartas se acerca más a 21 que la del Dealer.')
    print('4. Pierde si se pasa de 21 o el Dealer se acerca más.')
    print('==============================================================================')
modo = 0
modo = menu()
if modo == 1:
    como_jugar()
    modo = 2

if modo == 2: 
    #1. Declaración del jugador:
    nombre = input ('Ingrese un nombre: ')
    jugador1 = Jugador(nombre)
    dealer = Jugador('Dealer')

    #2. Un While que marque hasta que termine el juego
    while True: 
        ronda += 1   
        #3. Repartimos dos cartas al jugador:
        Dealer = Mazo()
        Dealer.mezclar()
        for i in range(2):
            jugador1.agregar(Dealer.repartir_una())
            dealer.agregar(Dealer.repartir_una())
        
        #4: Apuestas: 
        #Agregados
        if nombre == 'petu' and ronda == 1:
            jugador1.fichas += 999
            print ('Como usted es tan especial recibe 999 fichas')
            petu()
        if (nombre == 'silla' or nombre == '47' or nombre == 'Silla') and ronda == 1 :
            print ('Mucho gusto caballero. Usted recibe una cantidad basada de fichas ')
            jugador1.fichas += 46
            silla()
        if jugador1.fichas > 1:
            print(f'¿Cuanto quiere apostar? su presupuesto es: {jugador1.fichas}')
            while True:
                try: 
                    apuesta = int(input('Ingrese cuanto quiere apostar: '))
                except:
                    print ('Parece que no ingreso un valor permitido, intente devuelta.')
                else: 
                    if apuesta > jugador1.fichas:
                        print ('No tiene suficientes fichas')
                    elif apuesta == 0 or apuesta < 0:
                        print ('Valor invalido')
                    else: 
                        print ('¡Entendido!')
                        break
        else:
            print ('-----------------------------------------')
            print ('Usted ha apostado a única ficha que tenía')
            apuesta = 1
        jugador1.apostar(apuesta)
        print (f'Sus fichas restantes son: {jugador1.fichas}')
        
        #5 Calcular la suma de las cartas del jugador
        print ('Juego inicia:')
        print ('==========================')
        print (f'Las cartas del dealer son: \n 1.{dealer.mano[0]} \n 2. ??? ')
        print ('==========================')
        print ('Sus cartas son: ')
        cantidad = 0
        print ('======================================================')
        for i in range(0,len(jugador1.mano)):
            cantidad += 1
            print (f'La carta numero {cantidad} es: {jugador1.mano[i]}')
        print ('======================================================')
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
        print ('======================================')
        
        #7. Determinar si se pasa o no de 21: 
        if jugador1.suma() > 21:
            print (f'El jugador {jugador1.nombre} perdió. La suma de sus cartas pasó de 21')
            print(f'El jugador quedó con: {jugador1.fichas} fichas')
            if jugador1.fichas == 0:
                break
            else: 
                continue
        else: 
            print ('')
            print ('Le toca a la casa ahora:')
            print ('-------------------------------------------')
            print (f'Las cartas del Dealer son: \n 1. {dealer.mano[0]} \n 2. {dealer.mano[1]}')
            print (f'Y la suma de sus cartas es: {dealer.suma()}')
            print ('-------------------------------------------')
            if jugador1.suma() >= dealer.suma():
                while dealer.suma() <= jugador1.suma():
                    dealer.agregar(Dealer.repartir_una())
                    print (f'La carta agregada es {dealer.mano[-1]}')
                    print (f'Ahora la suma de sus cartas es: {dealer.suma()}')
                    print ('-----------------------------------------------')
                    
                    if dealer.suma() > 21:
                        print ('')
                        print (f'La suma de las cartas es: {dealer.suma()}')
                        print (f'Gana el jugador {jugador1.nombre}. La suma de las cartas del Dealer supero el máximo')
                        jugador1.gana(apuesta)
                        print (f'Como ganó el jugador sus fondos son: {jugador1.fichas}')
                        break
                    
                    elif dealer.suma() > jugador1.suma():
                        print ('')
                        print ('Gana la casa. El dealer tiene una suma mayor de cartas')
                        break
            
            elif dealer.suma() > jugador1.suma():
                print('El jugador pierde, gana la casa')
                print(f'El jugador quedó con: {jugador1.fichas} fichas')
                if jugador1.fichas == 0:
                    break
                else: 
                    continue
            
            else:
                print (f'Gana el jugador {jugador1.nombre}. Sus fichas son {jugador1.fichas}')
        #8. Preguntar si quiere seguir jugando y apostando sus fichas:
        while True:
            print('=====================================================')
            seguir = input('¿Quiere seguir jugando y apostar sus fichas? s = si n = no: ')
            if seguir == 's':
                print('=====================================================')
                break
            elif seguir == 'n':
                print('=====================================================')
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