from random import choice
import random
import time

def contar_puntos(jugador:list) -> int:
    diccionario = {f"{x[0]}": 0 for x in jugador }
    for carta in jugador:
        if carta[0] in diccionario:
            diccionario[carta[0]] += 1
        else:
            diccionario[carta[0]] = 1
    puntos = 0;
    
    for k,v in diccionario.items():
        if v == 2:
            if k in ['J','Q','K']:
                puntos += 11
            if k  == 'A':
                puntos += 12
            if k.isnumeric():
                puntos += int(k)
        if v == 3:
            if k in ['J','Q','K']:
                puntos += 110
            if k  == 'A':
                puntos += 120
            if k.isnumeric():
                puntos += int(k) *10
        if v == 4:
            if k in ['J','Q','K']:
                puntos += 1100
            if k  == 'A':
                puntos += 1200
            if k.isnumeric():
                puntos += int(k) * 100
    return puntos

def dar_carta(jugador:list, mazo:list)-> None:
    carta = choice(mazo)
    jugador.append(carta)
    mazo.remove(carta)
    
def mano_inicial(jugador:list, mazo:list) -> None:
    for i in range(5):
        dar_carta(jugador,mazo)
        
def crea_conteo(mano:list) -> dict:
    d = {}
    for carta in mano:
        if carta[0] in d:
            d[carta[0]]+=1
        else:
            d[carta[0]] = 1
    
    return d

def carta_mayor(dconteo:dict) -> str:
    d = {
        
        '?': 0,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }
    return max(dconteo, key=lambda key: d[key])

def hay_carta_repetida(mano_computadora:list) -> bool:
    if max(crea_conteo(mano_computadora).values()) > 1:
        return True
    else:
        return False
    
def hay_joker(mano:list) -> bool:
    if mano.__contains__('ඞ'):
        return True
    else:
        return False
def carta_repetida(mano:list) -> str:
    return max(crea_conteo(mano).values())
    
def dar_simbolo_aleatorio() -> str:
    return choice(["♠︎","♥︎","♣︎","♦︎"])

def asigna_simbolo(respuesta):
    simbolos = {
        '1': "♠︎",
        '2': "♥︎",
        '3': "♣︎",
        '4': "♦︎"
    }
    return simbolos[respuesta]

def asigna_joker_computadora(mano_computadora:list) -> list:
    
    if hay_carta_repetida(mano_computadora):
        mano_computadora.remove('ඞ')
        mano_computadora.append([carta_repetida(mano_computadora), dar_simbolo_aleatorio()])
    else:
        mano_computadora.remove('ඞ')
        mano_computadora.append([carta_mayor(mano_computadora), dar_simbolo_aleatorio()])
    

def asigna_joker_jugador(jugador:list):
    if hay_joker(jugador):
        valor = input(f"Elige el valor que quieres que tenga el joker: ")
        simbolo = input(f"Elige el simbolo♠,♥︎,♣︎,♦︎ : \n 1) ♠ \n 2) ♥︎ \n 3) ♣︎ \n 4) ♦︎ \n Respuesta : ")
        jugador.remove('ඞ')
        jugador.append([valor,asigna_simbolo(simbolo)])
        
    
    
def cambiar_carta(jugador:list,mazo:list):
    try:
        respuesta = input(f"¿Qué carta deseas cambiar? \n 1) {jugador[0]} \n 2){jugador[1]} \n 3) {jugador[2]} \n 4) {jugador[3]} \n 5) {jugador[4]} \n Respuesta: ")
        carta = jugador[int(respuesta)-1]
        jugador.remove(carta)
        dar_carta(jugador,mazo)
        print("\n")
        
    except:
        print("Nel papi; esa respuesta no es válida, intentalo de nuevo")
        cambiar_carta(jugador,mazo)
    
def cambiar_carta_aleatoria(mano_computadora:list,mazo:list):
    carta = choice(mano_computadora)
    mano_computadora.remove(carta)
    dar_carta(mano_computadora,mazo)
    
def hay_ganador(jugador:list, computadora:list,turno:int) -> bool:
    if turno >= 4:
            if contar_puntos(jugador) > contar_puntos(computadora):
                print (f"¡Ha ganado el jugador con {contar_puntos(jugador)} puntos!")
                return True
            elif contar_puntos(computadora) > contar_puntos(jugador):
                print (f"¡Ha ganado la computadora con {contar_puntos(computadora)} puntos!")
                return True
            else:
                return False

def crear_mazo() -> list:
    numeros = [f"{x}" for x in range (2,11)]
    letras = ["J","Q","K","A"]
    simbolos = ["♠︎","♥︎","♣︎","♦︎"]
    numeros.extend(letras)
    mazo = []
    for numero in numeros:
        for simbolo in simbolos:
            mazo.append([numero,simbolo])
    joker = "ඞ"
    mazo.extend(joker)
    return mazo
        
def jugar_pares():
    jugador = []
    computadora = []
    mazo = crear_mazo()
    
    mano_inicial(jugador,mazo)
    print(f"La mano del jugador es : {jugador} ")
    print (f"Los puntos del jugador son {contar_puntos(jugador)} \n")
    
    mano_inicial(computadora,mazo)
    print(f"La mano de la computadora es: {computadora}")
    print (f"Los puntos del jugador son {contar_puntos(computadora)} \n")
    
    en_juego = True
    turno = 0
    while(en_juego):
        print(f"Turno : {turno}")
        print("--------------------------------")
        # No se puede ganar antes del turno 4 nomás para hacerlo más divertido
        if hay_ganador(jugador,computadora,turno):
            respuesta = input("¿Deseas jugar otra partida?\n 1) Si \n 2) No \n Respuesta: ")
            if respuesta == '1':
                jugar_pares()
            else:
                break
        if turno % 2 == 0:
            cambiar_carta(jugador,mazo)
            if hay_joker(jugador):
                asigna_joker_jugador(jugador)
            print(f"La mano del jugador es : {jugador} ")
            print (f"Los puntos del jugador son {contar_puntos(jugador)} \n")
        else:
            time.sleep(4)
            cambiar_carta_aleatoria(computadora,mazo)
            if hay_joker(computadora):
                asigna_joker_computadora(computadora)
            print(f"La mano de la computadora es: {computadora}")
            print (f"Los puntos del jugador son {contar_puntos(computadora)} \n")
        if hay_ganador(jugador,computadora,turno):
            respuesta = input("¿Deseas jugar otra partida?\n 1) Si \n 2) No \n Respuesta: ")
            if respuesta == '1':
               jugar_pares()
            else:
                break
        turno += 1
        

def main():
    jugar_pares()
    
if __name__ == "__main__":
    main()
