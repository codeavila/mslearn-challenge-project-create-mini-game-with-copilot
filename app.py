import random

def jugar_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    puntaje_jugador = 0
    puntaje_oponente = 0

    while True:
        print("Elige una opción: piedra, papel o tijeras.")
        jugador = input("Tu elección: ").lower()
        if jugador not in opciones:
            print("Opción no válida. Por favor, elige piedra, papel o tijeras.")
            continue

        oponente = random.choice(opciones)
        print(f"El oponente elige: {oponente}")

        if jugador == oponente:
            print("Empate!")
        elif (jugador == "piedra" and oponente == "tijeras") or \
             (jugador == "papel" and oponente == "piedra") or \
             (jugador == "tijeras" and oponente == "papel"):
            print("¡Ganaste esta ronda!")
            puntaje_jugador += 1
        else:
            print("El oponente gana esta ronda.")
            puntaje_oponente += 1

        print(f"Puntaje actual - Jugador: {puntaje_jugador}, Oponente: {puntaje_oponente}")
        
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != "s":
            break

    print(f"Puntaje final - Jugador: {puntaje_jugador}, Oponente: {puntaje_oponente}")
    print("¡Gracias por jugar!")

if __name__ == "__main__":
    jugar_piedra_papel_tijeras()
