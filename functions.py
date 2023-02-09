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

def dar_carta(jugador:list, mazo:list)-> None:
    carta = choice(mazo)
    jugador.append(carta)
    mazo.remove(carta)
    
def mano_inicial(jugador:list, mazo:list) -> None:
    for i in range(5):
        dar_carta(jugador,mazo)
        

def main():
    numeros = [f"{x}" for x in range (2,11)]
    letras = ["J","Q","K","A"]
    simbolos = ["♠︎","♥︎","♣︎","♦︎"]
    numeros.extend(letras)
    mazo = []
    # mazo = [f"{list(zip(x[0],simbolos))}" for x in numeros]
    for numero in numeros:
        for simbolo in simbolos:
            mazo.append([numero,simbolo])
    joker = ["ඞ"]
    mazo.extend(joker)
    jugador = []
    computadora = []
    
    mano_inicial(jugador,mazo)
    print(f"La mano del jugador es : {jugador} ")
    print (f"Los puntos del jugador son {contar_puntos(jugador)} \n")
    
    mano_inicial(computadora,mazo)
    print(f"La mano de la computadora es: {computadora}")
    print (f"Los puntos del jugador son {contar_puntos(computadora)} \n")
    
    
if __name__ == "__main__":
    main()
