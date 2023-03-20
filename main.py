class Tablero:

    def __init__(self, filas:int, columnas:int, num_minas:int) -> None:
        
        self.filas = filas
        self.columnas = columnas
        self.num_minas = num_minas

    def crear_tablero(self, filas:int, columnas:int, num_minas:int):
        pass

    def mostrar_tablero(self):
        pass

    def abrir_celda(self, fila:int,columna:int):
        pass

    def poner_bandera(self, fila:int, columna:int):
        pass

class Jugador:

    def __init__(self) -> None:
        pass

    def unirse_al_juego(self, nombre:str):
        pass

    def enviar_mensaje(self, mensaje:str):
        pass

    def seleccionar_celda(self, fila:int, columna:int):
        pass

    def poner_bandera(self, fila:int, columna:int):
        pass

class Juego:

    def __init__(self) -> None:
        pass    

    def crear_juego(self, num_jugadores:int):
        pass

    def iniciar_juego(self):
        pass

    def actualizar_tablero(self, fila, columna, jugador):
        pass

    def enviar_mensaje(self, jugador, mensaje):
        pass

    def comprobar_juego_terminado(self):
        pass

class Interfaz:

    def __init__(self) -> None:
        pass

    def mostrar_tablero(self):
        pass

    def mostrar_chat(self):
        pass

    def capturar_seleccion(self):
        pass

    def capturar_bandera(self):
        pass