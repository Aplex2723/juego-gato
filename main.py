import random
run = True
tablero = [
	[" ", " ", " "], 
	[" ", " ", " "], 
	[" ", " ", " "]
	]

def poner(jugador, columna, fila):
	if jugador == 1:
		if tablero[fila-1][columna-1] == "O" or tablero[fila-1][columna-1] == "X":
			print("\n\tESTA CASILLA ESTA OCUPADA, PRUEBA NUEVAMENTE")
			return preguntarDatos(jugador)

		tablero[fila-1][columna-1] = "X"

		comprobarGanadorOEmpate()
	else:
		if tablero[fila-1][columna-1] == "X" or tablero[fila-1][columna-1] == "O":
			print("\n\tESTA CASILLA ESTA OCUPADA, PRUEBA NUEVAMENTE")
			return preguntarDatos(jugador)

		tablero[fila-1][columna-1] = "O"

		comprobarGanadorOEmpate()

def comprobarGanadorOEmpate():
	for i in range(len(tablero)):
		if tablero[i].count("X") == 3 or tablero[i].count("O") == 3:
			salir()
	for col in zip(*tablero):
		if col.count("X") == 3 or col.count("O") == 3:
			salir()

	diagonal1 = [row[i] for i, row in enumerate(tablero)]
	if diagonal1.count("X") == 3 or diagonal1.count("O") == 3:
		salir()
	diagonal2 = [row[2-i] for i, row in enumerate(tablero)]
	if diagonal2.count("X") == 3 or diagonal2.count("O") == 3:
		salir()

	libres = [(i, j) for j in random.sample(range(3), 3)
			for i in random.sample(range(3), 3)
			if vacia((i, j))]

	if not libres: empate()

def vacia(tupla):
	if tablero[tupla[0]][tupla[1]] == " ":
		return True
	else:
		return False

def empate():
	print("\t\nFUE UN EMPATE!")
	impirmirTablero()
	input("Pulsa cualquier letra para salir ...")
	exit()
			
def salir():
	print("\t\nFELIZIDADES, HAZ GANADO")
	impirmirTablero()
	input("Pulsa cualquier letra para salir ...")
	exit()

def impirmirTablero():
	print("\n")
	print("    1   2   3")
	print("  -------------")
	print(f"1 | {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} |")
	print("  -------------")
	print(f"2 | {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} |")
	print("  -------------")
	print(f"3 | {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} |")
	print("  -------------")
	print("\n")

def preguntarDatos(jugador):
	impirmirTablero()
	print((f"\tTurno del jugador {str(jugador)}"))
	fila = int(input("\nEscoge la fila: "))
	columna = int(input("Escoge la columna: "))

	if (columna > 3 or columna < 1 ) or (fila > 3 or fila < 1): 
		print("\n\tLos valores dados deben ser mayores a 3 o menores a 1, intentalo nuevamente")
		return preguntarDatos(jugador)
	
	poner(jugador, columna, fila)

def main():
    i = 0
    while run:
        jugador = i % 2 + 1
        preguntarDatos(jugador)
        i = i + 1


print(f"\tBIENVENIDO AL JUEGO")
main()