from random import choice

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

def obtener_carta(mazo:list)-> list:
    carta = choice(mazo)
    mazo.remove(carta)
    return carta
    
def obtener_mano(mazo:list) -> list:
    mano = []
    for i in range(5):
        mano.append(obtener_carta(mazo))
    return sorted(mano)

def cambiar_carta(jugador:list, mazo:list) -> None:
    carta_seleccionada = input(f"¿Qué carta deseas cambiar? \n 1) {jugador[0]} \n 2) {jugador[1]} \n 3) {jugador[2]} \n 4) {jugador[3]} \n 5) {jugador[4]}")
    jugador.remove(jugador[int(carta_seleccionada)-1])
    jugador = obtener_carta(mazo)
    sorted(jugador)
    
def verificar_jokers(jugador:list) -> list:
    jokers = []
    contador = 0
    for carta in jugador:
        if carta[1] == "ඞ":
            jokers.append(contador)
        contador += 1 
    return jokers
            
    
def cambiar_joker(jugador:list, pos_joker:list) -> None:
    nuevo_valor = ""
    if len(pos_joker) > 1:
        
        nuevo_valor = input("Asigna el valor del joker 1: ")
        jugador[pos_joker[0]][0] = nuevo_valor
        
        nuevo_valor = input("Asigna el valor del joker 2: ")
        jugador[pos_joker[1]][0] = nuevo_valor
        
    else:
        
        nuevo_valor = input("¿Qué valor deseas que tenga el joker ahora?")
        jugador[pos_joker[0]][0] = nuevo_valor

def inteligencia_computadora() -> None:
    print("a")
    


def jugar_pares(mazo:list) -> None:
    en_juego = True
    while en_juego:
        """
        Requisitos del juego
        
        - Debe de haber un marcador de partidas ganadas y perdidas
        - Se debe preguntar al usuario qué carta quiere dejar al jalar
        - La computadora debe tomar sus decisiones sola
        - El usuario elige cuando mostrar su mano para ganar
        - No se puede mostrar la mano antes del turno 5
        - Cuando se acaban las cartas del mazo se termina la partida
        - Debe haber un ganador o un empate
        - Se debe preguntar si se desea jugar de nuevo
        
        """
        
    
def jugar_21() -> None:
    print("21")

def main():
    numeros = [f"{x}" for x in range (2,11)]
    letras = ["J","Q","K","A"]
    simbolos = ["♠︎","♥︎","♣︎","♦︎"]
    numeros.extend(letras)
    mazo = []
    
    for numero in numeros:
        for simbolo in simbolos:
            mazo.append([numero,simbolo])
    joker = [["?","ඞ"],["?","ඞ"]]
    mazo.extend(joker)
    
    jugador = list(obtener_mano(mazo))
    computadora = list(obtener_mano(mazo))

    print(f"La mano del jugador es : {jugador} ")
    print (f"Los puntos del jugador son {contar_puntos(jugador)} \n")
    
    print(f"La mano de la computadora es: {computadora}")
    print (f"Los puntos del jugador son {contar_puntos(computadora)} \n")
    
    
        

if __name__ == "__main__":
    main()
