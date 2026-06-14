from game_modes.modo_base import ModoBase


class ModoX01(ModoBase):
    def __init__(self, puntuacion_inicial):
        self.nombre = str(puntuacion_inicial)
        self.puntuacion_inicial = puntuacion_inicial

    def aplicar_tirada(self, jugador, numero, multiplicador):
        puntos = numero * multiplicador
        nueva_puntuacion = jugador.puntuacion - puntos

        if nueva_puntuacion < 0:
            resultado = {
                "valida": True,
                "mensaje": f"{jugador.nombre} se ha pasado. Dardo fallado.",
                "ganador": False
            }

        else:
            jugador.puntuacion = nueva_puntuacion

            if jugador.puntuacion == 0:
                resultado = {
                    "valida": True,
                    "mensaje": f"{jugador.nombre} ha ganado",
                    "ganador": True
                }

            else:
                resultado = {
                    "valida": True,
                    "mensaje": f"{jugador.nombre} ha hecho {puntos} puntos",
                    "ganador": False
                }

        return resultado