from game_modes.modo_base import ModoBase


class ModoAroundTheClock(ModoBase):
    nombre = "Around the Clock"
    puntuacion_inicial = 1

    def aplicar_tirada(self, jugador, numero, multiplicador):
        if numero == jugador.puntuacion:
            jugador.puntuacion += 1

            if jugador.puntuacion > 20:
                return {
                    "valida": True,
                    "mensaje": f"{jugador.nombre} ha completado el reloj",
                    "ganador": True
                }

            return {
                "valida": True,
                "mensaje": f"{jugador.nombre} avanza al número {jugador.puntuacion}",
                "ganador": False
            }

        return {
            "valida": True,
            "mensaje": f"{jugador.nombre} no acertó el número objetivo",
            "ganador": False
        }