from random import randint

tablero=[]

for x in range(0,5):
    tablero.append(["0"] * 5)

def print_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

print_tablero(tablero)

def random_fila(tablero):
    return randint(0, len(tablero) - 1)

def random_col(tablero):
    return randint(0, len(tablero) - 1)

barco_fila = random_fila(tablero)
barco_col = random_fila(tablero)

# Muestra donde esta el barco
print(barco_fila)
print(barco_col)

for turno in range(4):
    print(f"Turno {turno+1}")

    ave_fila = int(input("Averigua la fila: "))
    ave_col = int(input("Averigua la columna: "))

    if ave_fila == barco_fila and ave_col == barco_col:
        print("Barco hundido!")
        print("Has ganado!")
        break
    else:
        if ave_fila > 5 or ave_col > 5:
            print("Fuera del tablero")
        elif tablero[ave_fila][ave_col]=="X":
            print("Ya has disparado en esas coordenadas")
        else:
            print("Fallo!")
            tablero[ave_fila][ave_col]="X"
            if turno==3:
                print("Fin del juego")
    print_tablero(tablero)
            
