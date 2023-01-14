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
            if i.valor() == 1 and len (self.mano) < 3 and resultado < 11: 
                while True:
                    try:
                        aux = int(input('Usted tiene un As ¿Cuanto quiere que valga 1 u 11? '))
                    except:
                        print ('Parece que no inserto un número, intente devuelta')
                        continue
                    else: 
                        if aux == 1 or aux == 11: 
                            print (f'¡Entendido, su As vale {aux}!')
                            break
                        else: 
                            print ('Usted no inserto un numero correcto, intente denuevo')
                            continue
                resultado += aux
            else:
                resultado += i.valor()
        return resultado    
    def __str__ (self):
        return (f'El jugador {self.nombre} tiene {len(self.mano)} cartas')