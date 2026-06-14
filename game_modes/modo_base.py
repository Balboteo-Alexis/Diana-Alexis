class ModoBase:
    nombre = "Modo Base"
    puntuacion_inicial = 0

    def aplicar_tirada(self, jugador, numero, multiplicador):
        raise NotImplementedError